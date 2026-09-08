# ECO-BRAIN — NEXT

## Single priority

Create the smallest repository-side verification artifact for the two existing ECO-BRAIN daily automations, without adding a new service or expanding architecture.

## Current verified milestone

The first **ECO-CEL Proof of Operation** is implemented, tested, demonstrated within its technical scope, merged into `main`, and verified by post-merge CI.

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
