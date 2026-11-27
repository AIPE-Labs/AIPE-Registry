# AIPE — AI for Power Engineering

Generated from validated capability manifests. Open-source first, commercial compatible.

Capabilities are **graduated** or **incubating**. The Registry assigns the stage; a repository cannot
declare itself graduated. Graduated means: reviewed, living under https://github.com/AIPE-Labs/ and pinned
here at a tagged release. Incubating capabilities are work in progress and may change or move.
The same information is machine-readable in `graduation.json`.

## Graduated capabilities

| Capability | Type | Maturity | Integration | Release | Canonical repository |
| --- | --- | --- | --- | --- | --- |
| AIPE Magnetics Database (`aipe.magnetics-database`) | tool | prototype | native | `v0.3.0` | [Repository](https://github.com/AIPE-Labs/AIPE-Magnetics-Database) |

## Incubating capabilities

| Capability | Type | Maturity | Integration | Release | Canonical repository |
| --- | --- | --- | --- | --- | --- |
| AIPE Academy (`aipe.academy`) | education | prototype | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Academy) |
| AIPE CAD Agent (`aipe.cad-agent`) | tool | prototype | none | untagged | [Repository](https://github.com/FulongLi/AIPE-CAD-Agent) |
| AIPE Core (`aipe.core`) | standard | prototype | native | untagged | [Repository](https://github.com/AIPE-Labs/AIPE-Core) |
| AIPE Doc (`aipe.doc`) | presentation | prototype | none | untagged | [Repository](https://github.com/FulongLi/AIPE-Doc) |
| AIPE Electrical Design (`aipe.electrical-design`) | tool | prototype | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Electrical-Design) |
| AIPE Field Simulation (`aipe.field-simulation`) | tool | prototype | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Field-Simulation) |
| AIPE IEEE Paper Agent (`aipe.ieee-paper-agent`) | agent | usable | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent) |
| AIPE Magnetics Design (`aipe.magnetics-design`) | tool | prototype | native | untagged | [Repository](https://github.com/FulongLi/AIPE-Magnetics-Design) |
| Open Engineering Tool Catalogue (`aipe.open-source-catalogue`) | catalogue | usable | none | untagged | [Repository](https://github.com/FulongLi/awesome-open-source-power-electronics) |
| AIPE PCB Agent (`aipe.pcb-agent`) | agent | prototype | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-PCB-Agent) |
| AIPE Labs Presentation (`aipe.presentation`) | presentation | prototype | none | untagged | [Repository](https://github.com/FulongLi/Spirit-Connect-AIPE-Labs) |
| AIPE Registry (`aipe.registry`) | registry | prototype | none | untagged | [Repository](https://github.com/AIPE-Labs/AIPE-Registry) |
| AIPE Semiconductor Database (`aipe.semiconductor-database`) | database | usable | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Semiconductor-Database) |
| AIPE Simulation Skills (`aipe.simulation-skills`) | skill_collection | usable | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Simulation-Skills) |
| AIPE Sketcher (`aipe.sketch`) | tool | usable | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Sketcher) |
| AIPE Thermal Design (`aipe.thermal-design`) | tool | prototype | mapped | untagged | [Repository](https://github.com/FulongLi/AIPE-Thermal-Design) |
| AIPE Workflows (`aipe.workflows`) | agent | prototype | native | untagged | [Repository](https://github.com/FulongLi/AIPE-Workflows) |

## AIPE Magnetics Database

Standardised, provenance-tracked magnetic data: material properties, core geometries and parts, measured core-loss tables, complex permeability / permittivity and B-H curves from Princeton MagNet, Paderborn LEA, OpenMagnetics MAS, HEFMAG and further sources in Magnetic Data Schema v0.2, with deduplication, licences, query API, CLI and a read-only MCP server.

Stage: **graduated**, release `v0.3.0`.

Capabilities: magnetics-record-schema, magnetics-data-import, magnetics-data-validation, magnetics-data-migration, magnetics-waveform-storage, magnetics-source-adapters, magnetics-material-lookup, magnetics-measurement-query, magnetics-data-provenance, magnetics-mcp-server, magnetics-agent-plugin.

Licence: `MIT`. Validation: `tested`.

- [Claude Code](https://code.claude.com/): free_proprietary; optional; interfaces: cli.
- [OpenAI Codex CLI](https://github.com/openai/codex): open_source; optional; interfaces: cli.
- [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk): open_source; optional; interfaces: mcp.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python, mcp.
- Limitation: Third-party values are unreviewed; many MAS values originate from manufacturer datasheets whose terms are not covered by the MAS licence.
- Limitation: Paderborn LEA records are GPL-3.0-only and kept as a separate copyleft subtree.
- Limitation: Code is MIT; every data record keeps the licence of its source (LICENSING.md), and the curated datasheet catalogue stays NOASSERTION.
- [Documentation: README.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/README.md)
- [Documentation: CHANGELOG.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/CHANGELOG.md)
- [Documentation: docs/data-format.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/data-format.md)
- [Documentation: docs/data-standard-v0.2.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/data-standard-v0.2.md)
- [Documentation: docs/source-catalogue.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/source-catalogue.md)
- [Documentation: docs/ingestion.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/ingestion.md)
- [Documentation: docs/provenance-and-limitations.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/provenance-and-limitations.md)
- [Documentation: docs/api.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/api.md)
- [Documentation: docs/migration-v0.3.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/docs/migration-v0.3.md)
- [Documentation: LICENSING.md](https://github.com/AIPE-Labs/AIPE-Magnetics-Database/blob/ea0e6a24838df71be045d2d85dfea22b506ea29a/LICENSING.md)

## AIPE Academy

Original, AI-native Power and Energy Engineering curriculum in four domains (Foundations, Power Electronics, Power Systems, Renewable Energy) with reproducible Python labs, a verified MIT OpenCourseWare academic baseline, and a shared Codex skill / Claude Code plugin.

Stage: **incubating**, no tagged release pinned.

Capabilities: guided-engineering-education, open-source-converter-labs, reproducible-engineering-labs, academic-reference-baseline, codex-skill, claude-code-plugin.

Licence: `CC-BY-4.0`. Validation: `tested`.

- [Matplotlib](https://matplotlib.org/): open_source; optional; interfaces: python.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Most modules remain outlines or planned; one complete reference lesson exists per domain.
- Limitation: Labs are ideal analytical or numerical teaching models, not hardware validation.
- Limitation: The MIT OpenCourseWare baseline is a scope reference; AIPE Academy is not affiliated with or endorsed by MIT.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Academy/blob/d98428c21ff6a77e4b8d16d9690a077efaa639c3/README.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-Academy/blob/d98428c21ff6a77e4b8d16d9690a077efaa639c3/docs/architecture.md)
- [Documentation: docs/curriculum-guide.md](https://github.com/FulongLi/AIPE-Academy/blob/d98428c21ff6a77e4b8d16d9690a077efaa639c3/docs/curriculum-guide.md)
- [Documentation: docs/plugin-installation.md](https://github.com/FulongLi/AIPE-Academy/blob/d98428c21ff6a77e4b8d16d9690a077efaa639c3/docs/plugin-installation.md)
- [Documentation: docs/website-integration.md](https://github.com/FulongLi/AIPE-Academy/blob/d98428c21ff6a77e4b8d16d9690a077efaa639c3/docs/website-integration.md)
- [Documentation: docs/ecosystem-v0.1.md](https://github.com/FulongLi/AIPE-Academy/blob/d98428c21ff6a77e4b8d16d9690a077efaa639c3/docs/ecosystem-v0.1.md)

## AIPE CAD Agent

Parametric FreeCAD geometry for power-converter transformers, plate-fin heat sinks, liquid cold plates and full converter assemblies, with STEP/FCStd export, mesh metadata and interference/clearance checks driven by JSON parameters in SI units.

Stage: **incubating**, no tagged release pinned.

Capabilities: parametric-transformer-cad, heat-sink-cad, cold-plate-cad, converter-assembly-cad, cad-interference-clearance-check.

Licence: `MIT`. Validation: `tested`.

- [CadQuery](https://cadquery.readthedocs.io/): open_source; optional; interfaces: python.
- [FreeCAD](https://www.freecad.org/): open_source; required; interfaces: cli, python.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Illustrative parametric models for layout, mass and clearance studies; not manufacturable designs and no DFM claims.
- Limitation: Windings are homogenised annular bodies with layer thickness derived from wire data; individual turns, lead-outs and bends are not modelled.
- Limitation: Clearance is measured as straight-line or one-bend air paths with Part.Shape.distToShape; creepage along insulating surfaces is not traced and conductors fully enclosed in insulation are reported for review.
- Limitation: Required clearance and creepage values are caller inputs; no compliance with any standard is asserted.
- Limitation: TDK E65/32/27 and Wolfspeed TO-247-4L dimensions are nominal values transcribed from the cited data sheets and must be verified against the current revisions.
- Limitation: No Engineering State adapter yet; integration with AIPE Core is planned, not implemented.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-CAD-Agent/blob/b81bf693389daa732dc9ee2c686ab3a897f26f81/README.md)
- [Documentation: docs/parameters.md](https://github.com/FulongLi/AIPE-CAD-Agent/blob/b81bf693389daa732dc9ee2c686ab3a897f26f81/docs/parameters.md)
- [Documentation: examples/dab-10kw/README.md](https://github.com/FulongLi/AIPE-CAD-Agent/blob/b81bf693389daa732dc9ee2c686ab3a897f26f81/examples/dab-10kw/README.md)

## AIPE Core

Versioned SI Engineering State schemas, evidence conventions and semantic interoperability contracts.

Stage: **incubating**, no tagged release pinned.

Capabilities: engineering-state-schema, engineering-evidence-contracts, offline-state-validation.

Licence: `MIT`. Validation: `tested`.

- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Schema and semantic checks do not prove engineering correctness or authenticate artifacts.
- Limitation: The checker resolves schemas from the local schemas/ directory and never downloads them.
- [Documentation: README.md](https://github.com/AIPE-Labs/AIPE-Core/blob/a8481c60ddfdced685067227fb16ca534be3eb5b/README.md)
- [Documentation: docs/metadata.md](https://github.com/AIPE-Labs/AIPE-Core/blob/a8481c60ddfdced685067227fb16ca534be3eb5b/docs/metadata.md)
- [Documentation: docs/architecture-v0.1.md](https://github.com/AIPE-Labs/AIPE-Core/blob/a8481c60ddfdced685067227fb16ca534be3eb5b/docs/architecture-v0.1.md)
- [Documentation: contracts/README.md](https://github.com/AIPE-Labs/AIPE-Core/blob/a8481c60ddfdced685067227fb16ca534be3eb5b/contracts/README.md)

## AIPE Doc

AIPE-branded HTML document and slide templates (A4 and 16:9 print layouts) with shared stylesheets, a link/asset validator and a preview server; the engineering review package of AIPE-Workflows is rendered in the document layout.

Stage: **incubating**, no tagged release pinned.

Capabilities: engineering-document-templates, html-report-presentation.

Licence: `NOASSERTION`. Validation: `schema_validated`.

- [Node.js](https://nodejs.org/): open_source; optional; interfaces: cli.
- Limitation: check.mjs validates local links, ids and language pairs of the shipped templates; it does not validate engineering content.
- Limitation: PDF export relies on the browser print engine; no automated PDF generation is included.
- Limitation: Repository content has no declared licence (NOASSERTION); brand assets are AIPE Labs material.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Doc/blob/9d2863378d176e5228efed4a1eb88eb8859c0e26/README.md)
- [Documentation: docs/guide.html](https://github.com/FulongLi/AIPE-Doc/blob/9d2863378d176e5228efed4a1eb88eb8859c0e26/docs/guide.html)
- [Documentation: templates/report-engineering.html](https://github.com/FulongLi/AIPE-Doc/blob/9d2863378d176e5228efed4a1eb88eb8859c0e26/templates/report-engineering.html)

## AIPE Electrical Design

Analytical electrical design models with explicit SI units and sign conventions - lossless single-phase-shift dual-active-bridge analysis, CCM DC-DC sizing and first-order buck losses - packaged as aipe_electrical. Formerly the AIPE Design Agent (id aipe.design-agent); the legacy PEA application is archived at Git tag legacy-pea-v0.1.

Stage: **incubating**, no tagged release pinned.

Capabilities: dab-sps-analysis, dab-sps-design-sweep, dcdc-ccm-sizing, buck-loss-first-order.

Licence: `MIT`. Validation: `tested`.

- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: The SPS model assumes ideal switches, zero dead time, stiff DC ports, an ideal transformer with negligible magnetising current and no losses; \|phi\| &lt;= pi/2.
- Limitation: ZVS results are necessary current-direction conditions of the lossless model, not charge-based ZVS verification.
- Limitation: CCM sizing uses the small-ripple approximation with ESR/ESL neglected; the buck loss estimate omits gate drive, Coss, reverse recovery, dead time and core loss.
- Limitation: The design-space sweep screens the electrical operating point only; losses, magnetics, thermal behaviour and cost are not modelled.
- Limitation: Mapping of results into Core engineering state is performed by the AIPE-Workflows adapter; this package emits unit-tagged quantities, not engineering-state documents.
- Limitation: Thermal models formerly under pea.thermal are provided by AIPE-Thermal-Design (aipe_thermal), not by this package.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Electrical-Design/blob/6e515ae040c8da9daf929c98e8584244e15521e6/README.md)
- [Documentation: docs/models.md](https://github.com/FulongLi/AIPE-Electrical-Design/blob/6e515ae040c8da9daf929c98e8584244e15521e6/docs/models.md)
- [Documentation: docs/migration.md](https://github.com/FulongLi/AIPE-Electrical-Design/blob/6e515ae040c8da9daf929c98e8584244e15521e6/docs/migration.md)
- [Documentation: CHANGELOG.md](https://github.com/FulongLi/AIPE-Electrical-Design/blob/6e515ae040c8da9daf929c98e8584244e15521e6/CHANGELOG.md)

## AIPE Field Simulation

Reproducible open-source field-simulation workflows (Gmsh meshing, ElmerGrid conversion, ElmerSolver FEM) for power-electronics thermal conduction, 2-D magnetostatics and 2-D eddy currents, with analytically verified benchmarks, mesh-convergence studies, DAB transformer-window and heat-sink parametric models, and AIPE evidence records (SI units, tool versions, SHA-256 artifacts).

Stage: **incubating**, no tagged release pinned.

Capabilities: fem-thermal-conduction, fem-magnetostatics-2d, fem-eddy-current-2d, analytic-benchmark-verification, simulation-case-provenance.

Licence: `MIT`. Validation: `tested`.

- [Elmer FEM (ElmerSolver, ElmerGrid)](https://www.elmerfem.org/): open_source; required; interfaces: cli, sif.
- [Gmsh](https://gmsh.info/): open_source; required; interfaces: python, cli.
- [OpenFOAM](https://www.openfoam.com/): open_source; optional; interfaces: cli.
- [Python](https://www.python.org/): open_source; required; interfaces: python, cli.
- Limitation: Tested means: unit tests of parsers/templating/analytic formulas plus end-to-end solver tests executed on Windows 11 with Gmsh 4.15.2 and Elmer 9.0 (recorded results) and on every push in GitHub Actions on Ubuntu 24.04 with Gmsh 4.15.2 and Elmer 26.2 from the ElmerCSC PPA, where a skipped solver test fails the job; locally the solver tests skip when the tools are absent.
- Limitation: Benchmarks are verified against closed-form solutions only; no measured validation of any transformer or heat-sink result.
- Limitation: The transformer AC winding-loss factor uses a homogenised solid-block conductivity and is an approximation indicator, not a Litz/foil loss prediction; 3-D transformer models are not provided.
- Limitation: CFD (OpenFOAM) is blocked on this platform; heat-sink film coefficients are supplied values.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/README.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/docs/architecture.md)
- [Documentation: examples/heatsink_to247/README.md](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/examples/heatsink_to247/README.md)
- [Documentation: examples/dab_10kw_heatsink/README.md](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/examples/dab_10kw_heatsink/README.md)
- [Documentation: results/benchmarks.md](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/results/benchmarks.md)
- [Documentation: docs/jobs/openfoam-heatsink-cfd-job.md](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/docs/jobs/openfoam-heatsink-cfd-job.md)
- [Documentation: LICENSE](https://github.com/FulongLi/AIPE-Field-Simulation/blob/63d2898f81905abab15c661d980563b273fe94dc/LICENSE)

## AIPE IEEE Paper Agent

Evidence-linked research planning and IEEE venue-specific manuscript production.

Stage: **incubating**, no tagged release pinned.

Capabilities: research-evidence-planning, ieee-manuscript-production.

Licence: `NOASSERTION`. Validation: `tested`.

- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Semantic Core mapping only; no automatic state converter.
- Limitation: Static checks do not verify citation truth or compile a PDF.
- Limitation: Repository-wide licence is unresolved; third-party assets retain rights.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/5192c621f4d1d53a40734aca62c0d180afc99194/README.md)
- [Documentation: docs/aipe-integration.md](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/5192c621f4d1d53a40734aca62c0d180afc99194/docs/aipe-integration.md)

## AIPE Magnetics Design

Evidence-first magnetic component design: consumes AIPE-Magnetics-Database (data standard v0.2), loss and hysteresis models with per-capability verification evidence, inductor/transformer design calculations, local MCP server and standalone Codex / Claude Code plugins.

Stage: **incubating**, no tagged release pinned.

Capabilities: magnetics-material-lookup, magnetics-material-comparison, magnetics-core-loss-estimation, magnetics-hysteresis-evaluation, magnetics-inductor-design, magnetics-transformer-design, magnetics-waveform-informed-transformer-design, magnetics-measurement-requests, magnetics-design-validation, magnetics-engineering-report, magnetics-verification-suite, magnetics-mcp-server, magnetics-agent-plugin, magnetics-core-state-export.

Licence: `NOASSERTION`. Validation: `tested`.

- [Claude Code](https://code.claude.com/): free_proprietary; optional; interfaces: cli.
- [OpenAI Codex CLI](https://github.com/openai/codex): open_source; optional; interfaces: cli.
- [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk): open_source; optional; interfaces: mcp.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python, mcp.
- [PyTorch](https://pytorch.org/): open_source; optional; interfaces: python.
- Limitation: Verification evidence is recorded per capability and operating range (levels L1-L3); there is no repository-wide validated flag.
- Limitation: Model implementations are verified against analytical, independent-numerical and published references (L2); no experimental (L3) validation is bundled.
- Limitation: Material and core parameters are datasheet-derived with locators and remain review_status unreviewed until an owner review.
- Limitation: No magnetic datasets are stored in this repository; all data come from AIPE-Magnetics-Database under its per-source licences.
- Limitation: Repository licence remains NOASSERTION pending owner decision.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/README.md)
- [Documentation: CHANGELOG.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/CHANGELOG.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/architecture.md)
- [Documentation: docs/audit-v0.1.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/audit-v0.1.md)
- [Documentation: docs/migration-v0.3.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/migration-v0.3.md)
- [Documentation: docs/models.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/models.md)
- [Documentation: docs/verification.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/verification.md)
- [Documentation: docs/api.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/api.md)
- [Documentation: docs/mcp.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/mcp.md)
- [Documentation: docs/plugins.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/plugins.md)
- [Documentation: docs/core-integration.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/core-integration.md)
- [Documentation: docs/sources.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/sources.md)
- [Documentation: docs/demo-dab-10kw.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/demo-dab-10kw.md)
- [Documentation: docs/waveform-informed-design.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/docs/waveform-informed-design.md)
- [Documentation: LICENSING.md](https://github.com/FulongLi/AIPE-Magnetics-Design/blob/ae9c4965eca6882d75e8252a4a7822f550366f88/LICENSING.md)

## Open Engineering Tool Catalogue

Community-curated external engineering tools with dated maintenance, licence and automation evidence.

Stage: **incubating**, no tagged release pinned.

Capabilities: external-tool-discovery, external-tool-maintenance-audit.

Licence: `NOASSERTION`. Validation: `tested`.

- [Python](https://www.python.org/): open_source; required; interfaces: cli.
- Limitation: No external solver or MCP execution validated. Catalogue inclusion does not imply AIPE support.
- [Documentation: README.md](https://github.com/FulongLi/awesome-open-source-power-electronics/blob/2ff81b28669d8c9a27a150eb2b2fd85bb70a76a5/README.md)
- [Documentation: CONTRIBUTING.md](https://github.com/FulongLi/awesome-open-source-power-electronics/blob/2ff81b28669d8c9a27a150eb2b2fd85bb70a76a5/CONTRIBUTING.md)
- [Documentation: generated/audit.md](https://github.com/FulongLi/awesome-open-source-power-electronics/blob/2ff81b28669d8c9a27a150eb2b2fd85bb70a76a5/generated/audit.md)

## AIPE PCB Agent

Reproducible KiCad 10 automation for power-electronics PCBs - deterministic hierarchical schematic and footprint-library generation from a shared part model, native board construction with courtyard- and insulation-aware placement, a reusable grid router, native kicad-cli ERC/DRC and export wrappers with hashed manifests, geometric layout checkers, a reference-derived engineering knowledge base, and requirement-file-driven generators (SiC buck V1-V3 and the 10 kW DAB three-board set).

Stage: **incubating**, no tagged release pinned.

Capabilities: kicad-schematic-generation, kicad-footprint-library-preparation, kicad-board-placement, grid-routing, native-erc-drc-verification, manufacturing-export-manifests, pcb-layout-metrics, insulation-coordination-rules, power-electronics-knowledge-retrieval, requirement-driven-pcb-generation.

Licence: `MIT`. Validation: `tested`.

- [KiCad 10 (kicad-cli, pcbnew Python)](https://www.kicad.org/): open_source; required; interfaces: cli, python.
- [Python](https://www.python.org/): open_source; required; interfaces: python, cli.
- Limitation: Tested means: 392 host-side unit tests (unittest/pytest) plus native kicad-cli ERC/DRC runs recorded as hashed manifests under the examples; nothing has been fabricated, energised or measured.
- Limitation: Zero native ERC/DRC findings are statements about the generated files under the recorded rule set; they establish neither electrical safety nor insulation compliance nor manufacturability. Insulation-coordination values are IEC 60664-1 reference inputs labelled to-be-reviewed.
- Limitation: Routing is a deterministic grid-router proposal; incomplete routings are reported as unresolved connections and remain visible in the DRC reports (see docs/dab-10kw/review-report.md for the DAB-V1 status).
- Limitation: Several pin tables and the controlCARD contact map of the DAB-V1 example are transcribed assumptions recorded in automation/dab_v1/parts.py and examples/dab-10kw/requirements/interfaces.yaml.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/README.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/docs/architecture.md)
- [Documentation: docs/agent-workflow.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/docs/agent-workflow.md)
- [Documentation: docs/pcb-design-rules.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/docs/pcb-design-rules.md)
- [Documentation: docs/knowledge-system.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/docs/knowledge-system.md)
- [Documentation: docs/dab-10kw/architecture-review.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/docs/dab-10kw/architecture-review.md)
- [Documentation: docs/dab-10kw/review-report.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/docs/dab-10kw/review-report.md)
- [Documentation: examples/dab-10kw/README.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/examples/dab-10kw/README.md)
- [Documentation: examples/sic-buck-400v-200v-5kw-v3/README.md](https://github.com/FulongLi/AIPE-PCB-Agent/blob/b0e0710085e3f9d6dc622b52a774f7630633334d/examples/sic-buck-400v-200v-5kw-v3/README.md)

## AIPE Labs Presentation

Jekyll presentation and stable public URLs for Registry capabilities and Academy lessons.

Stage: **incubating**, no tagged release pinned.

Capabilities: ecosystem-presentation, academy-publication.

Licence: `CC-BY-4.0`. Validation: `tested`.

- [Jekyll](https://jekyllrb.com/): open_source; required; interfaces: cli.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Presentation validation does not validate engineering claims.
- Limitation: Deployment follows reviewed PR merges; no live deployment performed.
- Limitation: Registry initialization has a local-only baseline until upstream empty-repository permissions are resolved.
- [Documentation: README.md](https://github.com/FulongLi/Spirit-Connect-AIPE-Labs/blob/5662ca2c56e77d8382ea7cfedcb9e63105219800/README.md)
- [Documentation: docs/ecosystem-v0.1.md](https://github.com/FulongLi/Spirit-Connect-AIPE-Labs/blob/5662ca2c56e77d8382ea7cfedcb9e63105219800/docs/ecosystem-v0.1.md)

## AIPE Registry

Discover and validate canonical AIPE capabilities and publish reproducible machine-readable and Markdown indexes.

Stage: **incubating**, no tagged release pinned.

Capabilities: capability-discovery, capability-manifest-validation, deterministic-registry-publication.

Licence: `MIT`. Validation: `tested`.

- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Core and Engineering State version identifiers are recognized; Registry does not transform engineering states.
- Limitation: Staging snapshots may precede upstream merge; inspect sources/snapshots.lock.json before deployment.
- Limitation: Snapshot-only checks cannot verify repository-relative documentation existence; use --checkouts for that audit.
- [Documentation: README.md](https://github.com/AIPE-Labs/AIPE-Registry/blob/85b2c71044d2deb6b93567ff5bf5f7af6792a914/README.md)
- [Documentation: CONTRIBUTING.md](https://github.com/AIPE-Labs/AIPE-Registry/blob/85b2c71044d2deb6b93567ff5bf5f7af6792a914/CONTRIBUTING.md)

## AIPE Semiconductor Database

Canonical V3 power semiconductor records with SI curves, source rights, evidence lineage, a conservative Core candidate adapter, DAB switch loss evaluation on actual waveform stress, evidence-tiered device screening, datasheet candidate import and prioritised measurement requests.

Stage: **incubating**, no tagged release pinned.

Capabilities: semiconductor-data, semiconductor-query, semiconductor-core-candidate-export, semiconductor-loss-evaluation, semiconductor-dab-screening, semiconductor-measurement-requests, candidate-device-import.

Licence: `NOASSERTION`. Validation: `tested`.

- [MATLAB](https://www.mathworks.com/products/matlab.html): commercial; optional; interfaces: file.
- [PLECS](https://www.plexim.com/plecs): commercial; optional; interfaces: file.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: Identity/source mapping only; detailed ratings and curves stay in V3 records.
- Limitation: Manufacturer model data is not converted into measured evidence.
- Limitation: Existing code and data rights remain NOASSERTION; see LICENSING.md.
- Limitation: DAB losses derive from manufacturer PLECS tensors and datasheet points; ZVS turn-on loss is zero by assumption without Coss/Eoss evidence.
- Limitation: Candidate device records are unreviewed datasheet transcriptions and are not canonical evidence.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Semiconductor-Database/blob/ba52e24dd2bce9d060a4ec81cc4f74ab3ded7db4/README.md)
- [Documentation: docs/dab-loss-screening.md](https://github.com/FulongLi/AIPE-Semiconductor-Database/blob/ba52e24dd2bce9d060a4ec81cc4f74ab3ded7db4/docs/dab-loss-screening.md)
- [Documentation: docs/core-integration.md](https://github.com/FulongLi/AIPE-Semiconductor-Database/blob/ba52e24dd2bce9d060a4ec81cc4f74ab3ded7db4/docs/core-integration.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-Semiconductor-Database/blob/ba52e24dd2bce9d060a4ec81cc4f74ab3ded7db4/docs/architecture.md)
- [Documentation: LICENSING.md](https://github.com/FulongLi/AIPE-Semiconductor-Database/blob/ba52e24dd2bce9d060a4ec81cc4f74ab3ded7db4/LICENSING.md)
- [Documentation: data/candidates/README.md](https://github.com/FulongLi/AIPE-Semiconductor-Database/blob/ba52e24dd2bce9d060a4ec81cc4f74ab3ded7db4/data/candidates/README.md)

## AIPE Simulation Skills

Engineering-purpose simulation, control, CAD, PCB and field-analysis skills with an open-source default and preserved optional proprietary workflows, plus the executable aipe_simulation package: ngspice qualification and batch runner, dual-active-bridge switching-circuit generator (ideal and behavioural levels) and a solver-independent waveform analysis engine (HDF5 datasets, steady-state detection, per-switch metrics).

Stage: **incubating**, no tagged release pinned.

Capabilities: averaged-control-analysis, switching-circuit-simulation, mechanical-packaging, pcb-power-stage-review, field-analysis-problem-setup, digital-control-debugging, dab-switching-circuit-generation, waveform-analysis-engine, solver-tool-qualification.

Licence: `NOASSERTION`. Validation: `tested`.

- [ANSYS](https://www.ansys.com/): commercial; optional; interfaces: scripting.
- [CalculiX](https://www.calculix.de/): open_source; optional; interfaces: cli, inp.
- [COMSOL](https://www.comsol.com/): commercial; optional; interfaces: java-api, batch.
- [Elmer FEM](https://github.com/ElmerCSC/elmerfem): open_source; optional; interfaces: cli, sif.
- [FreeCAD](https://www.freecad.org/): open_source; optional; interfaces: python, cli.
- [GetDP](https://getdp.info/): open_source; optional; interfaces: cli, pro.
- [Gmsh](https://gmsh.info/): open_source; optional; interfaces: cli, python.
- [KiCad](https://www.kicad.org/): open_source; optional; interfaces: cli, ipc, python.
- [LTspice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html): free_proprietary; optional; interfaces: batch, netlist.
- [MATLAB / Simulink](https://www.mathworks.com/products/simulink.html): commercial; optional; interfaces: matlab, batch.
- [ngspice](https://ngspice.sourceforge.io/): open_source; optional; interfaces: cli, netlist.
- [openEMS](https://www.openems.de/): open_source; optional; interfaces: python, octave.
- [PLECS](https://www.plexim.com/plecs): commercial; optional; interfaces: scripting, xml-rpc.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- [python-control](https://python-control.org/): open_source; optional; interfaces: python.
- [SIMetrix / SIMPLIS](https://www.simetrix.co.uk/): commercial; optional; interfaces: scripting, netlist.
- Limitation: Local Python numerical tests passed; ngspice solver tests (tests/test_dab_ngspice.py, marker 'solver') ran against ngspice 47 on Windows and are skipped when ngspice is absent.
- Limitation: Executed DAB simulations are Level 1 ideal and Level 2 behavioural models with datasheet-sourced parameters; no manufacturer SPICE model (Level 3) has been executed or validated.
- Limitation: FreeCAD, KiCad, FEA solvers and MCP connectors are not executed by this repository; their skills remain procedural guidance.
- Limitation: No measurements or full Engineering State round-trip adapter claimed; AIPE-Workflows maps the run outputs into Core evidence.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/README.md)
- [Documentation: docs/tool-policy.md](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/docs/tool-policy.md)
- [Documentation: docs/core-mapping.md](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/docs/core-mapping.md)
- [Documentation: skills.json](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/skills.json)
- [Documentation: docs/validation.md](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/docs/validation.md)
- [Documentation: docs/dab-models.md](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/docs/dab-models.md)
- [Documentation: pyproject.toml](https://github.com/FulongLi/AIPE-Simulation-Skills/blob/1301c89ea9630d458c1136e15b2c1861002c5090/pyproject.toml)

## AIPE Sketcher

AI-powered electrical schematic generation for power electronics and circuit engineering. Renders explicit Circuit IR into connectivity-checked SVG schematics with validation reports and provenance; installable as a Codex and Claude Code plugin.

Stage: **incubating**, no tagged release pinned.

Capabilities: schematic-generation, circuit-connectivity-validation.

Licence: `LicenseRef-AIPE-Sketcher-Personal-NonCommercial-0.1 AND CC0-1.0`. Validation: `tested`.

- [Claude Code](https://code.claude.com/): free_proprietary; optional; interfaces: cli, gui.
- [OpenAI Codex](https://github.com/openai/codex): open_source; optional; interfaces: cli, gui.
- [Inkscape](https://inkscape.org/): open_source; optional; interfaces: cli, gui.
- [Python](https://www.python.org/): open_source; required; interfaces: python, cli.
- Limitation: Explicit Circuit IR and complete Core validation are required separately; no device sizing or physical results are inferred.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/README.md)
- [Documentation: docs/README.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/docs/README.md)
- [Documentation: docs/plugins.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/docs/plugins.md)
- [Documentation: docs/cli.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/docs/cli.md)
- [Documentation: docs/engineering-state.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/docs/engineering-state.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/docs/architecture.md)
- [Documentation: LICENSE](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/LICENSE)
- [Documentation: THIRD_PARTY_NOTICES.md](https://github.com/FulongLi/AIPE-Sketcher/blob/57a343e91b4005b14f57e2bc51685de6a5f4a983/THIRD_PARTY_NOTICES.md)

## AIPE Thermal Design

Analytical thermal design evaluation for power semiconductors and their cooling (SI units): plate-fin heat-sink correlation model (natural and forced convection, pressure drop and fan operating point, fin efficiency, spreading resistance, heat-load solve, seeded Pareto optimiser), steady-state shared-sink thermal networks with Foster/Cauer transient impedances, loss(Tj) &lt;-> Tj electrothermal iteration, natural / forced-air / liquid cold-plate comparison with explicit review items, Stage A heat-sink geometry screening with junction-limit checks, and the AIPE 10 kW DAB case. No CFD, FEM or measured values.

Stage: **incubating**, no tagged release pinned.

Capabilities: thermal-network-steady-state, thermal-network-transient-foster-cauer, electrothermal-iteration, cooling-concept-comparison, heatsink-correlation-model, heatsink-pareto-optimisation, heatsink-stage-a-screening, thermal-design-constraints.

Licence: `CC-BY-4.0 AND MIT`. Validation: `tested`.

- [Python with NumPy and SciPy](https://www.python.org/): open_source; required; interfaces: python, cli.
- Limitation: Tested means: analytic limit checks of every correlation, migrated unit tests of the networks, electrothermal loop, cooling comparison, screening and CLI, and regression comparisons against the numbers recorded by the AIPE DAB workflow run of 2026-10-21 (cooling 63.0 / 64.3 / 79.2 degC, Stage A knee 0.4405 K/W and 0.2783 kg, heat-sink model 1.426012 K/W and 1.609200 kg).
- Limitation: No CFD, FEM or measured validation of any heat sink, cold plate or device temperature; Stage B (FEM/CFD) is only flagged, not performed.
- Limitation: The DAB case uses stated placeholders (reference-design turn-off loss, same-family R_DS(on) temperature factor); device losses should come from the semiconductor database evaluator.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Thermal-Design/blob/177ad34a0084d7d7b1765e6d3b51300938962e14/README.md)
- [Documentation: docs/models.md](https://github.com/FulongLi/AIPE-Thermal-Design/blob/177ad34a0084d7d7b1765e6d3b51300938962e14/docs/models.md)
- [Documentation: docs/validation.md](https://github.com/FulongLi/AIPE-Thermal-Design/blob/177ad34a0084d7d7b1765e6d3b51300938962e14/docs/validation.md)
- [Documentation: CHANGELOG.md](https://github.com/FulongLi/AIPE-Thermal-Design/blob/177ad34a0084d7d7b1765e6d3b51300938962e14/CHANGELOG.md)
- [Documentation: LICENSES.md](https://github.com/FulongLi/AIPE-Thermal-Design/blob/177ad34a0084d7d7b1765e6d3b51300938962e14/LICENSES.md)
- [Documentation: docs/legacy/heat_sink_optimization_summary.html](https://github.com/FulongLi/AIPE-Thermal-Design/blob/177ad34a0084d7d7b1765e6d3b51300938962e14/docs/legacy/heat_sink_optimization_summary.html)

## AIPE Workflows

System-level engineering workflow engine executing typed, checkpointed task graphs over AIPE specialist capabilities (electrical and thermal design, simulation skills, semiconductor and magnetics databases, field simulation, CAD and PCB agents), with local tool qualification, Engineering State provenance, cross-module feedback iterations, verification gates and report assembly; first benchmark is the simulation-driven 10 kW dual-active-bridge converter.

Stage: **incubating**, no tagged release pinned.

Capabilities: engineering-workflow-execution, workflow-task-graph, capability-discovery-client, environment-tool-qualification, engineering-state-provenance, verification-gate-ledger, engineering-report-assembly.

Licence: `MIT`. Validation: `tested`.

- [Elmer FEM](https://github.com/ElmerCSC/elmerfem): open_source; optional; interfaces: cli, sif.
- [FreeCAD](https://www.freecad.org/): open_source; optional; interfaces: cli, python.
- [Gmsh](https://gmsh.info/): open_source; optional; interfaces: python, cli.
- [KiCad](https://www.kicad.org/): open_source; optional; interfaces: cli.
- [ngspice](https://ngspice.sourceforge.io/): open_source; optional; interfaces: cli.
- [Python](https://www.python.org/): open_source; required; interfaces: cli, python.
- Limitation: The DAB reference run executes analytical design, ngspice Levels 1 and 2, waveform-informed magnetics, device screening and losses, SPS control baseline, cooling comparison and heat-sink screening, Gmsh/Elmer window and heat-sink FEM, and FreeCAD transformer and heat-sink geometry; PCB boards are produced by AIPE-PCB-Agent outside the task graph and CFD, manufacturer SPICE models (Level 3), measurement and hardware stages are not executed.
- Limitation: Specialist results are analytical correlations, manufacturer data or executed numerical models with stated validity ranges; none is a measured value.
- Limitation: A completed workflow run establishes software and simulation gates only; engineering review, experimental measurement and hardware qualification are separate statuses that this engine never asserts.
- Limitation: Capability discovery reads manifests as data; it does not execute connectors or install software.
- [Documentation: README.md](https://github.com/FulongLi/AIPE-Workflows/blob/6284f1864a1dbabbc089f9194f9f03056aedcf13/README.md)
- [Documentation: docs/architecture.md](https://github.com/FulongLi/AIPE-Workflows/blob/6284f1864a1dbabbc089f9194f9f03056aedcf13/docs/architecture.md)
- [Documentation: docs/execution-envelope.md](https://github.com/FulongLi/AIPE-Workflows/blob/6284f1864a1dbabbc089f9194f9f03056aedcf13/docs/execution-envelope.md)
- [Documentation: docs/capability-matrix.md](https://github.com/FulongLi/AIPE-Workflows/blob/6284f1864a1dbabbc089f9194f9f03056aedcf13/docs/capability-matrix.md)
- [Documentation: workflows/converter_dab/README.md](https://github.com/FulongLi/AIPE-Workflows/blob/6284f1864a1dbabbc089f9194f9f03056aedcf13/workflows/converter_dab/README.md)
- [Documentation: examples/dab-10kw/README.md](https://github.com/FulongLi/AIPE-Workflows/blob/6284f1864a1dbabbc089f9194f9f03056aedcf13/examples/dab-10kw/README.md)
