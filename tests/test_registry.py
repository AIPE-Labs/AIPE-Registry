import copy
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_registry
import refresh
import registry


@pytest.fixture
def manifest():
    value = registry.read_yaml(ROOT / "aipe.yaml")
    value["dependencies"] = []
    return value


def entry(manifest, root=None, provenance=None):
    return {"manifest": manifest, "root": root, "provenance": provenance or {}}


def errors(manifests):
    return [d for d in registry.validate([entry(m) for m in manifests]) if d["severity"] == "error"]


@pytest.fixture
def sources(tmp_path, manifest):
    directory = tmp_path / "sources"
    directory.mkdir()
    source = {"id": manifest["id"], "repository": manifest["repository"], "ref": "a" * 40, "state": "pinned", "path": "aipe.yaml"}
    path = directory / "repositories.yaml"
    path.write_text(yaml.safe_dump({"schema_version": "0.1.0", "repositories": [source]}), encoding="utf-8")
    snapshot = directory / "snapshots" / "registry.yaml"
    snapshot.parent.mkdir()
    data = yaml.safe_dump(manifest).encode()
    snapshot.write_bytes(data)
    lock = {"schema_version": "0.1.0", "sources": [{**source, "snapshot": "snapshots/registry.yaml", "sha256": registry.sha256(data), "commit": "a" * 40, "committed_at": "2026-10-07T00:00:00Z", "manifest_dirty": False, "origin": "remote"}]}
    (directory / "snapshots.lock.json").write_text(registry.json_text(lock), encoding="utf-8")
    return path


def test_schema_accepts_own_shape(manifest):
    registry.Draft202012Validator.check_schema(json.loads((ROOT / 'schema/capability-manifest.schema.json').read_text()))
    assert errors([manifest]) == []


@pytest.mark.parametrize("mutate", [
    lambda m: m.update(unknown="typo"),
    lambda m: m.pop("repository"),
    lambda m: m.update(id="Bad ID"),
    lambda m: m.update(type="monolith"),
    lambda m: m.update(schema_version="0.2.0"),
    lambda m: m["compatibility"].update(core="1.x"),
    lambda m: m["compatibility"].update(integration="certified"),
    lambda m: m["tools"][0].update(licence_class="commercial", optional=False),
    lambda m: m["tools"][0].update(licence_class="free_proprietary", optional=False),
    lambda m: m["tools"][0].update(url="not-a-uri"),
    lambda m: m.update(extensions={"unscoped": {}}),
    lambda m: m["inputs"][0].update(schema="relative/path"),
    lambda m: m["inputs"][0].update(schema="https://example.com/space in uri"),
    lambda m: m["dependencies"].append({"id": "aipe.core", "version": "1.x", "optional": False}),
])
def test_invalid_manifest_rejected(manifest, mutate):
    mutate(manifest)
    assert errors([manifest])


@pytest.mark.parametrize("data", ["id: aipe.one\nid: aipe.two", "value: .nan", "date: 2026-10-07", "x: !!python/object:bad {}", "x: &x [*x]", "? [complex, key]\n: value"])
def test_unsafe_or_non_json_yaml_rejected(data):
    with pytest.raises(registry.RegistryError):
        registry.parse_yaml(data)


def test_yaml_12_boolean_words_are_strings():
    assert registry.parse_yaml('id: on\nname: yes\nenabled: false') == {'id': 'on', 'name': 'yes', 'enabled': False}


def test_missing_uri_checker_fails_closed(manifest, monkeypatch):
    monkeypatch.delitem(registry.FormatChecker.checkers, 'uri')
    with pytest.raises(registry.RegistryError, match='format validation'):
        registry.validate([entry(manifest)])


def test_duplicate_id_and_unknown_optional_dependency(manifest):
    duplicate = copy.deepcopy(manifest)
    assert any(d["code"] == "duplicate_id" for d in errors([manifest, duplicate]))
    manifest["dependencies"] = [{"id": "aipe.missing", "version": "0.1.x", "optional": True}]
    assert any(d["code"] == "unknown_dependency" for d in errors([manifest]))


def test_dependency_cycle(manifest):
    other = copy.deepcopy(manifest)
    other.update(id="aipe.other", repository="https://github.com/FulongLi/AIPE-Other")
    manifest["dependencies"] = [{"id": other["id"], "version": "0.1.x", "optional": False}]
    other["dependencies"] = [{"id": manifest["id"], "version": "0.1.x", "optional": False}]
    assert any(d["code"] == "dependency_cycle" for d in errors([manifest, other]))


def test_connector_must_reference_declared_tool(manifest):
    manifest["connectors"] = [{"id": "unknown", "tool": "missing", "type": "api", "repository": "https://example.com/api", "license": "MIT", "status": "evaluated", "supported_versions": [], "platforms": ["linux"], "security_notes": ["Review before running."]}]
    assert any(d["code"] == "unsupported_connector_tool" for d in errors([manifest]))


def test_diagnostics_are_read_only_and_repeatable(manifest, tmp_path):
    manifest.update(status="deprecated", license="NOASSERTION")
    manifest["tools"][0].update(licence_class="commercial", optional=True, interfaces=[])
    original = copy.deepcopy(manifest)
    diagnostic = registry.validate([entry(manifest, tmp_path, {"committed_at": "2020-01-01T00:00:00Z"})], today=dt.date(2026, 10, 7))
    assert {"stale_repository", "legacy_replacement", "unresolved_license", "documentation_drift", "unsupported_tool", "missing_open_alternative"} <= {d["code"] for d in diagnostic}
    assert manifest == original


@pytest.mark.parametrize("reference", ["../private.txt", "%2e%2e/private.txt", "https://example.com/../safe"])
def test_reference_confinement(manifest, reference):
    manifest["documentation"] = [reference]
    found = errors([manifest])
    assert bool(found) == (not reference.startswith("https://"))


def test_network_is_opt_in_and_failures_are_reported(monkeypatch, manifest):
    calls = []
    def fail(request, timeout):
        calls.append(request.full_url)
        raise OSError("test dead link")
    monkeypatch.setattr(registry, "urlopen", fail)
    registry.validate([entry(manifest)])
    assert calls == []
    result = registry.validate([entry(manifest)], check_links=True)
    assert calls and any(d["code"] == "dead_link" for d in result)


def test_offline_build_deterministic_and_tamper_fails_without_partial_write(sources, tmp_path, monkeypatch):
    def no_network(*args, **kwargs):
        raise AssertionError("offline build attempted network")
    monkeypatch.setattr(registry, "urlopen", no_network)
    first, second = tmp_path / "one", tmp_path / "two"
    assert build_registry.main(["--sources", str(sources), "--output-dir", str(first)]) == 0
    assert build_registry.main(["--sources", str(sources), "--output-dir", str(second)]) == 0
    for name in ("aipe.json", "aipe.md"):
        assert (first / name).read_bytes() == (second / name).read_bytes()
    assert build_registry.main(["--sources", str(sources), "--output-dir", str(first), "--check"]) == 0
    original = (first / "aipe.json").read_bytes()
    (sources.parent / "snapshots/registry.yaml").write_text("id: tampered", encoding="utf-8")
    assert build_registry.main(["--sources", str(sources), "--output-dir", str(first)]) == 1
    assert (first / "aipe.json").read_bytes() == original


def test_missing_snapshot_fails_complete_discovery(sources):
    (sources.parent / "snapshots/registry.yaml").unlink()
    with pytest.raises(registry.RegistryError):
        registry.discover(sources)


def test_source_lock_drift_and_duplicate_source_rejected(sources):
    document = registry.read_yaml(sources)
    document["repositories"][0]["ref"] = "b" * 40
    sources.write_text(yaml.safe_dump(document), encoding="utf-8")
    with pytest.raises(registry.RegistryError, match="drift"):
        registry.discover(sources)
    document["repositories"].append(document["repositories"][0])
    sources.write_text(yaml.safe_dump(document), encoding="utf-8")
    with pytest.raises(registry.RegistryError, match="duplicate"):
        registry.source_records(sources)


def test_build_output_order_independent_of_discovery_order(manifest):
    other = copy.deepcopy(manifest)
    other.update(id="aipe.another", repository="https://github.com/FulongLi/AIPE-Another")
    left = registry.document([entry(manifest), entry(other)])
    right = registry.document([entry(other), entry(manifest)])
    assert registry.json_text(left) == registry.json_text(right)
    assert registry.markdown(left) == registry.markdown(right)
    assert set(left) == {"schema_version", "capabilities"}


def test_malformed_lock_fails_with_actionable_error(sources):
    (sources.parent / 'snapshots.lock.json').write_text('{"schema_version":"0.1.0","sources":[{}]}')
    with pytest.raises(registry.RegistryError, match='provenance fields'):
        registry.discover(sources)


def test_markdown_uses_observed_revision_and_marks_unpublished_sources(manifest):
    payload = registry.document([entry(manifest)])
    published = {manifest['id']: {'commit': 'a' * 40, 'state': 'pending_pr', 'ref': 'refs/pull/1/head'}}
    assert '/blob/' + 'a' * 40 + '/README.md' in registry.markdown(payload, published)
    published[manifest['id']]['ref'] = 'codex/staged'
    assert 'publication pending' in registry.markdown(payload, published)
    assert '/blob/' not in registry.markdown(payload, published)


def test_remote_refresh_resolves_branch_once_then_fetches_commit(sources, manifest, monkeypatch):
    doc = registry.read_yaml(sources)
    doc["repositories"][0].update(ref="feature", state="pending_pr")
    sources.write_text(yaml.safe_dump(doc), encoding="utf-8")
    urls = []
    commit = "c" * 40
    def fetch(url):
        urls.append(url)
        if "api.github.com" in url:
            return json.dumps({"sha": commit, "commit": {"committer": {"date": "2026-10-07T00:00:00Z"}}}).encode()
        return yaml.safe_dump(manifest).encode()
    monkeypatch.setattr(refresh, "fetch", fetch)
    assert refresh.refresh(sources, remote=True) == 1
    assert len(urls) == 2 and f"/{commit}/aipe.yaml" in urls[1]
    assert registry.discover(sources)[0]["provenance"]["commit"] == commit


def test_refresh_failure_preserves_snapshot_lock(sources, monkeypatch):
    lock_path = sources.parent / "snapshots.lock.json"
    before = lock_path.read_bytes()
    monkeypatch.setattr(refresh, "fetch", lambda url: (_ for _ in ()).throw(OSError("offline")))
    with pytest.raises(OSError):
        refresh.refresh(sources, remote=True)
    assert lock_path.read_bytes() == before


@pytest.mark.parametrize("script", ["discover.py", "validate.py", "build_registry.py", "refresh.py"])
def test_cli_help(script):
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / script), "--help"], capture_output=True, text=True)
    assert result.returncode == 0 and "usage:" in result.stdout


LABS = "https://github.com/AIPE-Labs/AIPE-Registry"


def rewrite_source(sources, **changes):
    """Apply the same change to the source list and its lock, as a refresh would."""
    document = registry.read_yaml(sources)
    document["repositories"][0].update(changes)
    sources.write_text(yaml.safe_dump(document), encoding="utf-8")
    lock_path = sources.parent / "snapshots.lock.json"
    lock = json.loads(lock_path.read_text())
    lock["sources"][0].update(changes)
    lock_path.write_text(registry.json_text(lock), encoding="utf-8")


@pytest.mark.parametrize("changes, message", [
    ({"stage": "graduated"}, "tagged release"),
    ({"stage": "graduated", "release": "v0.1.0", "repository": "https://github.com/FulongLi/AIPE-Registry"}, "must live under"),
    ({"stage": "finished"}, "stage must be"),
    ({"release": "latest"}, "version tag"),
    ({"release": "v0.1.0", "state": "pending_pr", "ref": "refs/pull/1/head"}, "pinned commit"),
])
def test_graduation_rule_is_enforced_by_the_source_list(sources, changes, message):
    document = registry.read_yaml(sources)
    document["repositories"][0].update({"repository": LABS, **changes})
    sources.write_text(yaml.safe_dump(document), encoding="utf-8")
    with pytest.raises(registry.RegistryError, match=message):
        registry.source_records(sources)


def test_manifest_cannot_declare_itself_graduated(manifest):
    for field in ("stage", "release", "graduated"):
        claimed = {**manifest, field: "graduated"}
        assert any(e["code"] == "schema" for e in errors([claimed]))


def test_stage_change_without_refresh_is_lock_drift(sources):
    assert registry.discover(sources)[0]["provenance"].get("stage") is None
    document = registry.read_yaml(sources)
    document["repositories"][0].update(stage="graduated", release="v0.1.0")
    sources.write_text(yaml.safe_dump(document), encoding="utf-8")
    with pytest.raises(registry.RegistryError, match="drift"):
        registry.discover(sources)


def test_graduated_listed_first_and_index_envelope_unchanged(sources, manifest, tmp_path):
    assert manifest["repository"] == LABS
    rewrite_source(sources, stage="graduated", release="v0.1.0")
    out = tmp_path / "out"
    assert build_registry.main(["--sources", str(sources), "--output-dir", str(out)]) == 0
    assert set(json.loads((out / "aipe.json").read_text())) == {"schema_version", "capabilities"}
    stages = json.loads((out / "graduation.json").read_text())
    assert stages["capabilities"] == {manifest["id"]: {"stage": "graduated", "release": "v0.1.0", "commit": "a" * 40, "repository": LABS}}
    text = (out / "aipe.md").read_text()
    assert "Stage: **graduated**, release `v0.1.0`." in text
    assert text.index("## Graduated capabilities") < text.index(f"(`{manifest['id']}`)") < text.index("## Incubating capabilities")

    other = copy.deepcopy(manifest)
    other.update(id="aipe.aaa", name="Earlier Name", repository="https://github.com/FulongLi/AIPE-Other")
    payload = registry.document([entry(other), entry(manifest)])
    text = registry.markdown(payload, {manifest["id"]: {"stage": "graduated", "release": "v0.1.0", "commit": "a" * 40}})
    assert text.index("## AIPE Registry") < text.index("## Earlier Name")
    assert "Stage: **incubating**, no tagged release pinned." in text
    assert registry.graduation([entry(other)])["capabilities"]["aipe.aaa"]["stage"] == "incubating"


def test_remote_refresh_rejects_release_tag_on_another_commit(sources, manifest, monkeypatch):
    document = registry.read_yaml(sources)
    document["repositories"][0].update(stage="graduated", release="v0.1.0")
    sources.write_text(yaml.safe_dump(document), encoding="utf-8")
    before = (sources.parent / "snapshots.lock.json").read_bytes()
    tag_commit = ["b" * 40]

    def fetch(url):
        if url.endswith("/commits/v0.1.0"):
            return json.dumps({"sha": tag_commit[0]}).encode()
        if "api.github.com" in url:
            return json.dumps({"sha": "a" * 40, "commit": {"committer": {"date": "2026-10-07T00:00:00Z"}}}).encode()
        return yaml.safe_dump(manifest).encode()
    monkeypatch.setattr(refresh, "fetch", fetch)
    with pytest.raises(registry.RegistryError, match="release v0.1.0"):
        refresh.refresh(sources, remote=True)
    assert (sources.parent / "snapshots.lock.json").read_bytes() == before
    tag_commit[0] = "a" * 40
    assert refresh.refresh(sources, remote=True) == 1
    assert registry.discover(sources)[0]["provenance"]["release"] == "v0.1.0"


def test_checked_in_graduates_meet_the_rule():
    graduated = [r for r in registry.source_records() if r.get("stage") == "graduated"]
    assert graduated, "at least one graduated capability is expected"
    for record in graduated:
        assert record["repository"].startswith(registry.GRADUATED_ORGANISATION) and record["release"] and record["state"] == "pinned"
