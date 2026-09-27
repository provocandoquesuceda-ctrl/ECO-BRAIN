# Capability Core — Architecture v0.1

## Purpose

Convert the existing 120 capability units into productive, reusable infrastructure for the ecosystem without rebuilding them from zero.

The repository remains the operational home of ECO-BRAIN. The Capability Core is an additive layer: it indexes, contracts, consumes, composes and verifies capabilities while preserving the identity of existing implementations and repositories.

## Operating model

`CAP → contract → consumer → GitHub execution → evidence → reuse → composition → new capability`

A capability is not considered productive merely because it is catalogued. The productive unit is a demonstrated consumption that produces recoverable evidence.

## Non-destructive rules

1. Do not reconstruct the 120 capabilities merely to register them.
2. Do not copy a source implementation into a consumer when a contract/interface is sufficient.
3. Preserve native repository identity and native execution.
4. Add a capability to the operational registry when its source, identity, contract, evidence and consumption path can be established.
5. Prefer capabilities with strong evidence and low adaptation cost.
6. Compose capabilities only when the composition has a concrete use and can be verified.
7. Every verified reuse becomes a candidate pattern for subsequent consumers.
8. Existing working systems are improved, not replaced.

## Repository role

The Capability Core is a capability provider, not a monolithic replacement for ecosystem repositories.

Consumers may include:
- ECO-BRAIN
- VERCELOPS
- ECO-AUTOMATIONS
- L-DOGMA
- future ecosystem repositories

## Layers

### 1. Registry
Machine-readable inventory of capability identities, status, contracts, evidence and consumers.

### 2. Contracts
Stable interfaces describing what a capability guarantees and what a consumer must provide/produce.

### 3. Consumers
Repository-native implementations that consume a capability without surrendering their own identity.

### 4. Compositions
Verified combinations of two or more capabilities that produce a useful higher-level result.

### 5. Evidence
Traceable execution records: capability/contract → consumer → commit → workflow/run → output/artifact → result.

### 6. Automation
GitHub workflows and later automation that validate, consume and verify capabilities.

## First proven pattern

TRACE+VERIFY is the first operational pattern to use as the mold:

- Source contract: `contracts/trace-verify-v0.1.json`
- Consumer: VERCELOPS
- Consumer implementation: `scripts/trace-verify-consumer.mjs`
- Required outcome: real GitHub Actions execution with recoverable run ID and artifact/evidence

The pattern is not declared fully closed until the execution evidence is recoverable.

## Promotion rule

A capability progresses through:

`IDENTIFIED → CONTRACTED → VERIFIED → CONSUMABLE → REUSED → COMPOSED`

Only evidence-backed transitions are promoted.

## Success metrics

The core should eventually expose, from evidence rather than manual estimates:

- total CAP units
- verified CAP units
- consumable CAP units
- verified consumptions
- repositories consuming capabilities
- reuse count per CAP
- compositions
- derived capabilities
- evidence artifacts
- blocked/adaptation-required consumers

The objective is not the size of the registry. The objective is measurable productive output.
