# CrowdStrike Falcon Events Data Dictionary

> An open, searchable, machine-readable reference of **CrowdStrike Falcon sensor events** — exported to **CSV** and **Markdown** for threat hunting, detection engineering, SIEM onboarding, and **AI/LLM ingestion**.

[![License: Apache 2.0](https://img.shields.io/github/license/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary)](LICENSE)
<!-- BADGES:START (auto-updated by app/extract_events.py — do not edit between these markers) -->
[![Events documented](https://img.shields.io/badge/events-998-blue)](data/current/sensor_events.md)
[![Data updated](https://img.shields.io/badge/data-2026--06--02-success)](data/current/)
<!-- BADGES:END -->
[![Last commit](https://img.shields.io/github/last-commit/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary)](https://github.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/commits/main)
[![Stars](https://img.shields.io/github/stars/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary?style=social)](https://github.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/stargazers)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)

The official CrowdStrike Falcon **Events Data Dictionary** is enormous (1,500+ pages) and lives behind authentication, which makes it hard to search, diff, or feed into tooling. This repository turns that PDF into **clean, versioned, plain-text data** that you can grep, query, diff across releases, and load directly into an LLM or a SIEM.

<!-- LATEST:START (auto-updated by app/extract_events.py — do not edit between these markers) -->
**Latest snapshot:** [`data/2026-06-02/`](data/2026-06-02/) — **998 sensor events** across Windows, Linux, macOS, iOS, Android, ChromeOS, Falcon Container, Kubernetes, Public Cloud, and Forensics.
<!-- LATEST:END -->

Need a link that never goes stale? [`data/current/`](data/current/) always mirrors the newest snapshot.

- Source documentation (auth required): <https://docs.crowdstrike.com/r/en-US/sensormap.ftmap>

---

## 🤖 Use it with AI / LLMs (RAG, agents, chatbots)

These exports are designed to be dropped straight into a prompt, a vector store, or a retrieval pipeline. They are plain UTF-8, ~300&nbsp;KB, and contain one row/section per event with its description and supported platforms.

**Stable raw URLs (no auth needed):**

`data/current/` always mirrors the newest snapshot, so these URLs never change between releases. Pin to a dated folder (e.g. `data/2026-06-02/`) instead if you need a fixed version.

```text
# Markdown (best for RAG / LLM context windows)
https://raw.githubusercontent.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/main/data/current/sensor_events.md

# CSV (best for dataframes, embeddings, SQL)
https://raw.githubusercontent.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/main/data/current/sensor_events.csv

# Machine-readable index for AI agents
https://raw.githubusercontent.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/main/llms.txt
```

**Quick start for an LLM pipeline:**

```python
import pandas as pd

URL = ("https://raw.githubusercontent.com/erickatwork/"
       "CrowdStrike-Falcon-Events-Data-Dictionary/main/data/current/sensor_events.csv")
events = pd.read_csv(URL)

# Build documents for a vector store / RAG index
docs = [
    f"{row.header}: {row.description} (Platforms: {row.platforms})"
    for row in events.itertuples()
]
print(len(docs), "Falcon event documents ready for embedding")
```

See [`llms.txt`](llms.txt) for an AI-agent-friendly map of this repository.

**Ready-made AI instructions** (the data fits in one context window — no RAG needed):

- [`skills/crowdstrike-falcon-events/`](skills/crowdstrike-falcon-events/SKILL.md) — a **Claude Skill** that auto-loads when you ask about Falcon events (Claude Code / Desktop / API).
- [`prompts/system-prompt.md`](prompts/system-prompt.md) — a **copy-paste system prompt** for any LLM (ChatGPT, Gemini, etc.).

---

## 📁 What's inside

```
data/
  current/                     # auto-mirror of the newest snapshot (stable raw URLs)
    sensor_events.csv
    sensor_events.md
    SOURCE.md                  # which dated snapshot this mirrors
  2026-06-02/                  # versioned snapshot (ISO date)
    Events Full Reference.pdf  # original CrowdStrike export
    sensor_events.csv          # events: header, description, platforms
    sensor_events.md           # same data + table of contents + summary table
  2025-10-24/                  # previous snapshot (for diffing changes over time)
app/
  extract_events.py            # PDF -> CSV + Markdown extractor (also refreshes current/ + docs)
  examine_pdf.py               # inspect / search the raw PDF
```

Each snapshot is kept in its own ISO-dated directory so you can **diff the schema between releases** and track when events are added, removed, or change platform support. `data/current/` is generated automatically and should not be edited by hand.

## 🔎 Data format

### CSV

```csv
header,description,platforms
AccessoryDisconnected,"Sent when a device disconnects from an external accessory...","Android, iOS"
ActiveDirectoryAccountDisabled,"Indicates the subject account has been disabled.",Windows
```

### Markdown

- Linked table of contents for every event
- A summary table (event, description, platforms)
- A detailed section per event

## 🚀 Re-generate the data yourself

```bash
# 1. Install uv (https://docs.astral.sh/uv/getting-started/installation/)
curl -LsSf https://astral.sh/uv/install.sh | sh   # macOS/Linux

# 2. Get the PDF: visit the source documentation (auth required) at
#    https://docs.crowdstrike.com/r/en-US/sensormap.ftmap and export it as a PDF.
#    Drop it into a dated folder, e.g. data/2026-06-02/Events Full Reference.pdf

# 3. Extract (auto-detects the most recent dated folder under data/)
uv run app/extract_events.py
```

Outputs `sensor_events.csv` and `sensor_events.md` next to the PDF. When the PDF you extract is the **newest** dated snapshot, the extractor also self-updates the repo: it refreshes `data/current/`, the README badges and "Latest snapshot" line, and `llms.txt` — so a new export is the only manual step.

```bash
# Point at a specific PDF
uv run app/extract_events.py "data/2026-06-02/Events Full Reference.pdf"

# Write outputs elsewhere
uv run app/extract_events.py -o output/
```

### Inspect the PDF

```bash
uv run app/examine_pdf.py                  # first pages of newest PDF
uv run app/examine_pdf.py -p 30 -n 5       # pages 30-34
uv run app/examine_pdf.py --search DnsRequest
```

## 🔧 Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- `pdfplumber` (installed automatically via `uv sync`)

## 🧭 How the extractor works

The reference PDF prints each event with its title repeated on two lines, followed by `Platforms:`, an optional description, then per-platform `Fields:` tables:

```
AccessoryDisconnected
AccessoryDisconnected
Platforms: Android, iOS
Sent when a device disconnects from an external accessory...
Fields: Android
Field Description
...
```

`extract_events.py` flattens the document (stripping running headers/footers), reads the numbered table of contents as an authoritative whitelist, and emits one record per event. The run is validated against the table of contents so you can see if any event was missed.

## 🗂 Keywords

CrowdStrike Falcon, Falcon sensor events, CrowdStrike events data dictionary, Falcon Data Replicator (FDR), CrowdStrike event schema, EDR telemetry, endpoint detection and response, threat hunting, detection engineering, SIEM onboarding, Splunk, CrowdStrike Query Language (CQL), Falcon LogScale / Humio, security data dictionary, ProcessRollup2, DnsRequest, NetworkConnectIP4, incident response, blue team, SOC.

## ⚖️ Disclaimer

This is an **unofficial, community-maintained** project and is **not affiliated with, endorsed by, or sponsored by CrowdStrike**. "CrowdStrike" and "Falcon" are trademarks of CrowdStrike, Inc. The event definitions are the property of CrowdStrike and are shared here for reference and interoperability. If you are a CrowdStrike customer, always treat the [official documentation](https://docs.crowdstrike.com/r/en-US/sensormap.ftmap) as the source of truth.

## 🤝 Contributing

Contributions are welcome — especially **new dated snapshots** when CrowdStrike updates the dictionary, parser improvements, and tooling for diffing releases. Please open an issue or pull request.

## 📝 License

Released under the [Apache License 2.0](LICENSE). The underlying event definitions remain the property of CrowdStrike, Inc.
