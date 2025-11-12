# Lease Analytics

A modular Python project for analyzing car lease data — including fuel economy, km/month,
and spending categories — with a NiceGUI + Plotly dashboard.

## Quick Start

```bash
uv venv
uv pip install -e .[dev]
uv run analytics --gui
```

Data is stored in `data/db/lease_analytics.db` and imported from `data/raw/*.csv`.
