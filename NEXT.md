# ECO-BRAIN — NEXT

## Single priority

Complete and verify the first **ECO-CEL Proof of Operation**.

## Cycle

`OBSERVAR → ANALIZAR → PRIORIZAR → PREPARAR → EJECUTAR/PROPONER → VERIFICAR → REGISTRAR → ACTUALIZAR → REPETIR`

## Current next action

Run the automated test suite for the ECO-CEL control-cycle skeleton and preserve the result as evidence.

## Verification note

The first CI attempt exposed an import-path issue in the test runner. The workflow was corrected to run with `PYTHONPATH=.`; a new verification run is required.

## After verification

1. Confirm the cycle is genuinely demonstrated.
2. Update `STATUS.md` with verified evidence.
3. Connect the two existing ECO-BRAIN daily automations to this cycle with the minimum necessary prompt changes.
4. Do not add another service/platform unless a concrete blocker requires it.
