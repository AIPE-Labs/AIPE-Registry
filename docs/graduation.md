# Graduated and incubating capabilities

Every capability in the index has a **stage**:

- **graduated** — reviewed, finished enough to depend on, living in the
  [AIPE-Labs](https://github.com/AIPE-Labs) organisation and pinned here at a
  tagged release;
- **incubating** — everything else: work in progress that may change, move or
  be renamed.

The Registry is the gate. A repository cannot declare itself graduated: the
stage is not a manifest field (the manifest schema rejects unknown fields), it
is set in [`sources/repositories.yaml`](../sources/repositories.yaml) through a
reviewed pull request to this repository.

## The rule the build checks

A source record may carry two optional fields:

```yaml
- {id: aipe.magnetics-database, repository: 'https://github.com/AIPE-Labs/AIPE-Magnetics-Database',
   ref: ea0e6a24838df71be045d2d85dfea22b506ea29a, state: pinned, path: aipe.yaml,
   stage: graduated, release: v0.3.0}
```

- `release` names a version tag (`vMAJOR.MINOR.PATCH`). It requires
  `state: pinned`, and `ref` must be the commit of that tag. `refresh.py`
  verifies this against GitHub (`--remote`) or the checkout's tags
  (`--checkouts`) and refuses to write the lock if the tag is missing or points
  elsewhere.
- `stage: graduated` requires `release` and a repository under
  `https://github.com/AIPE-Labs/`. A record without `stage` is incubating.

Both fields are copied into `sources/snapshots.lock.json`. The offline build
fails on any difference between the source list and the lock, so a stage cannot
be changed without a refresh that re-verifies the tag.

The mechanical rule is necessary, not sufficient. Before a pull request sets
`stage: graduated`, the reviewer confirms the
[graduation checklist](https://github.com/AIPE-Labs/.github/blob/main/GRADUATION.md)
kept with the organisation.

## Where the stage is published

- `generated/aipe.md` lists graduated capabilities first, labels the rest as
  incubating, and states the stage and release in each capability section.
- `generated/graduation.json` is the machine-readable form:
  `{"schema_version", "rule", "capabilities": {<id>: {"stage", "repository",
  "commit", "release"?}}}`.
- `generated/aipe.json` is unchanged: exactly `schema_version` and
  `capabilities`, each a complete manifest. Existing consumers that check this
  envelope keep working; read `graduation.json` alongside it for the stage.

## Graduating a capability

1. Transfer the repository to AIPE-Labs and update `repository` in its
   `aipe.yaml`.
2. Publish a tagged release from the default branch.
3. In `sources/repositories.yaml`, set the organisation address, `ref` to the
   tag's commit, `release` to the tag and `stage: graduated`.
4. Run `refresh.py`, `build_registry.py` and the tests; open a pull request.
