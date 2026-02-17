# Fix for Pipeline PREP_STATE_SHA Bug

## Problem
Pipeline fails in APPLY phase with error: "prep.json missing PREP_STATE_SHA"

Root cause: prepare.py saves `prep_state_sha` (snake_case) but artifacts.py validates `PREP_STATE_SHA` (UPPER_CASE).

## Solution
1. prepare.py: Add `PREP_STATE_SHA` key to prep.json (alongside `prep_state_sha` for compatibility)
2. artifacts.py: Accept either `PREP_STATE_SHA` or `prep_state_sha` for backward compatibility

## Changes
```python
# file: core/pipeline/prepare.py
# action: replace
# old: prep_json = asdict(result)
        artifacts.write_artifact("prep", result.task_id, "prep.json", prep_json)
# new: prep_json = asdict(result)
        # Compatibilidad: APPLY espera PREP_STATE_SHA (UPPER)
        prep_json["PREP_STATE_SHA"] = result.prep_state_sha
        artifacts.write_artifact("prep", result.task_id, "prep.json", prep_json)
```

```python
# file: core/pipeline/artifacts.py
# action: replace
# old: if "PREP_STATE_SHA" not in prep:
                raise ValidationError("prep.json missing PREP_STATE_SHA")
# new: # Compatibilidad: aceptar PREP_STATE_SHA o prep_state_sha
            if "PREP_STATE_SHA" not in prep and "prep_state_sha" not in prep:
                raise ValidationError("prep.json missing PREP_STATE_SHA")
```

## Verification
```bash
# Test that pipeline completes without PREP_STATE_SHA error
python -c "from core.pipeline_runner import PipelineRunner; print('OK')"
```
