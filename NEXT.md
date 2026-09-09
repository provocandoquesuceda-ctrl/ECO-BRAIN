# ECO-BRAIN — NEXT

## Single priority

Create the smallest repository-side verification artifact for the two existing ECO-BRAIN daily automations, without adding a new service or expanding architecture.

## Current verified milestone

The first **ECO-CEL Proof of Operation** is implemented, tested, demonstrated within its technical scope, merged into `main`, and verified by post-merge CI.

## Governance milestone (2026-09-08)

The **Marco de Escalabilidad Operacional del Ecosistema de Ecosistemas v1.0** has been formally approved and registered in `docs/MARCO-ESCALABILIDAD-OPERACIONAL-ECOSISTEMA-DE-ECOSISTEMAS-v1.0.md`.

The approval establishes the problematization scale 0–10, execution/autonomy scale E0–E9, recursive ECO-CEL, evidence discipline, minimum verifiable increment, separation of capacity from authority, and mandatory human governance for strategic/sensitive/irreversible decisions.

Approval of the framework does **not** imply implementation of all future capabilities.

## Automation verification result (2026-09-08)

Both daily automations are configured and enabled in the automation layer. Repository inspection found no automation-specific code/configuration, test, workflow, or execution artifact proving that either automation invokes or records the repository ECO-CEL cycle.

## Verification discipline

`DISEÑADO → IMPLEMENTADO → PROBADO → DEMOSTRADO → COMPLETADO`

No stage is inferred from the previous one. Each status requires repository or execution evidence.

## Current next action

Define and implement only a minimal, reversible verification artifact that can answer:

1. whether an automation run can observe the current repository state;
2. whether it can record the ECO-CEL cycle result;
3. whether CI can validate the artifact;
4. whether execution evidence exists.

## Decision gate

Do not move to ECAL or add external infrastructure until this minimum automation-verification increment is either demonstrated or blocked by concrete evidence.

## Constraint

Do not add another service/platform unless a concrete blocker requires it. Keep strategic, sensitive, and irreversible decisions under mandatory human governance.
