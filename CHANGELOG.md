# Changelog

## 0.1.0 — 2026-11-27

First tagged release, published from the AIPE-Labs organisation.

- Capability-manifest schema 0.1.0 (JSON Schema 2020-12) with fail-closed
  validation of identity, dependencies, tools, connectors and references.
- Offline, deterministic build of `generated/aipe.json` and `generated/aipe.md`
  from SHA-256-pinned manifest snapshots.
- Graduation gate: `stage` and `release` in the source list, verified on
  refresh and checked by the build; `generated/graduation.json`; graduated
  capabilities listed first in `generated/aipe.md`. See `docs/graduation.md`.
- Index of 18 capabilities at their current commits; AIPE-Magnetics-Database
  `v0.3.0` is the first graduate.
