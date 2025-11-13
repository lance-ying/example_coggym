# Ying et al. (2025) Understanding Dataset

## Overview
- Curated stimuli and human response data for replicating the experiments from Ying et al. (2025).
- Organized into two experiments (`exp1`, `exp2`) with corresponding configuration, instruction, stimuli, and human response files.
- Assets include GIF/PNG stimulus renderings grouped by trial identifiers.

## Directory Structure
- ``exp1/``: primary experiment assets and metadata.
- ``exp2/``: secondary experiment with segmented stimulus assets.

## Key Files
- ``config.json``: high-level experiment metadata and `experimentFlow` definition.
- ``instruction.jsonl`` (exp1): participant instructions aligned with config blocks.
- ``stimuli.jsonl`` / ``stimuli.json``: full trial definitions referenced by `stimuli_id`.
- ``human_data_ind.json``: individual participant responses.
- ``human_data_mean.json``: aggregated responses.
- ``assets/``: visual stimuli folders (`icon/`, `stimuli/`, or `segments/`) keyed by trial IDs.

## Using the Data
- Pair each block in `config.json` with trials defined in the stimuli file using matching `stimuli_id`.
- Render instructions and trials in the order specified by `experimentFlow`; apply randomization flags per block definition.
- Human response files use trial IDs identical to those in `stimuli.jsonl`/`stimuli.json`, enabling straightforward joins.

## Related Documentation
- Refer to ``documentation/config_schema.html`` for the full configuration schema.
- See ``documentation/trial_schema.html`` and ``documentation/instruction_schema.html`` for trial and instruction formats.
- Human data schema details are available in ``documentation/human_data_schema.html``.

