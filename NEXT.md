# ECO-BRAIN — NEXT

## Single priority

Verify the two existing ECO-BRAIN daily automations against the now-verified ECO-CEL cycle before designing any new capability.

## Current verified milestone

The first **ECO-CEL Proof of Operation** is implemented, tested, demonstrated within its technical scope, merged into `main`, and verified by post-merge CI.

## Verification discipline

`DISEÑADO → IMPLEMENTADO → PROBADO → DEMOSTRADO → COMPLETADO`

No stage is inferred from the previous one. Each status requires repository or execution evidence.

## Current next action

Locate the two existing daily automations in the repository and verify, for each one:

1. whether it exists in code/configuration;
2. whether it invokes or is connected to the ECO-CEL cycle;
3. whether tests or CI evidence exist;
4. whether there is execution evidence;
5. what, if anything, is missing or failing.

## Decision gate

Only after that verification will ECO-BRAIN determine whether connecting the automations is the next implementation increment or whether another capability, including ECAL, is justified.

## Constraint

Do not add another service/platform unless a concrete blocker requires it. Keep strategic, sensitive, and irreversible decisions under mandatory human governance.
