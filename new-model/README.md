# New Model Fallback

This directory contains a fresh fallback dissertation and journal-paper model:

State-dependent oil-price pass-through to India's WPI Fuel and Power inflation, 1994-2026.

## Run

From the repository root:

```bash
Rscript new-model/R/run_all.R
```

The script rebuilds processed data, tables, figures, diagnostics, and publication gates.

## Main outputs

- Processed data: `data/processed/model_dataset.csv`
- Main all-sample estimates: `outputs/tables/table_05_lp_all_sample.csv`
- Post-2010 state-dependent estimates: `outputs/tables/table_06_lp_post2010.csv`
- Diagnostics: `outputs/tables/table_10_diagnostics.csv`
- Publication triage: `outputs/tables/table_11_publication_triage.csv`
- Dissertation blueprint: `docs/blueprint.md`
- Journal blueprint: `docs/journal_paper_publishing_blueprint.md`
