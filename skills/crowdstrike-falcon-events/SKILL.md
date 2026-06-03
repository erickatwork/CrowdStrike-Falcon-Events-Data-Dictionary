---
name: crowdstrike-falcon-events
description: >-
  Answer questions about CrowdStrike Falcon sensor events using a community
  data dictionary of 998 events (name, description, supported platforms). Use
  this whenever the user asks what a Falcon event means, which events exist for
  a platform (Windows/Linux/macOS/iOS/Android/ChromeOS/Falcon Container/
  Kubernetes/Public Cloud/Forensics), how to map events for threat hunting,
  detection engineering, SIEM/Splunk onboarding, FDR (Falcon Data Replicator),
  or CrowdStrike event-schema work.
license: Apache-2.0
---

# CrowdStrike Falcon Events Data Dictionary

A searchable reference of **998 CrowdStrike Falcon sensor events**, extracted
from the official (auth-gated, 1,500+ page) PDF into clean plain text. Each
record has three fields: `header` (the event name), `description`
(human-readable), and `platforms` (comma-separated list of supported OSes /
sensor environments).

## When to use this skill

Use it for any question about CrowdStrike Falcon **sensor events**, e.g.:

- "What does `DnsRequest` / `ProcessRollup2` / `NetworkConnectIP4` mean?"
- "Which events fire on macOS only?" / "List all Active Directory events."
- "What event should I hunt on for process execution on Linux?"
- "Map Falcon events to MITRE ATT&CK / build a Splunk or CQL detection."
- "Diff the event schema between two snapshots."

Do **not** use it as authoritative for production detections — it is an
unofficial community export. Always cite the official docs as source of truth.

## How to load the data

The dataset is small (~340 KB Markdown ≈ ~85K tokens) and fits directly into a
modern context window. Prefer loading the whole file into context over building
a vector store.

1. **If this repository is available locally**, read the latest snapshot:
   - `data/current/sensor_events.md` (best for reading/answering — always the newest)
   - `data/current/sensor_events.csv` (best for filtering/tables)
   - `data/current/` is an auto-maintained mirror of the newest ISO-dated folder
     (e.g. `data/2026-06-02/`); read a dated folder directly if you need a fixed snapshot.

2. **Otherwise, fetch the stable raw URLs** (no auth required; `current` always
   points at the latest release):
   - Markdown: `https://raw.githubusercontent.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/main/data/current/sensor_events.md`
   - CSV: `https://raw.githubusercontent.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/main/data/current/sensor_events.csv`
   - Repo map for agents: `https://raw.githubusercontent.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary/main/llms.txt`

If you cannot read or fetch the file, say so explicitly rather than guessing
from memory.

## Data format

Markdown layout (`sensor_events.md`):
- A linked **Table of Contents** of all event names.
- A **Summary Table**: `| Header | Description | Platforms |` (descriptions truncated).
- A **detailed section per event**:

```text
### DnsRequest

**Description:** <full description, may be empty for undocumented events>

**Platforms:** Windows, Linux, macOS
```

CSV layout (`sensor_events.csv`): `header,description,platforms` — one row per
event. The `platforms` column is a quoted, comma-separated list.

Notes on the data:
- Some events have an empty `description` (undocumented in the source PDF). Say
  so rather than inventing a definition.
- `platforms` values include OSes and sensor environments: Windows, Linux,
  macOS, iOS, Android, ChromeOS, Falcon Container, Kubernetes, Public Cloud,
  Vmcluster, Forensics.

## How to answer

1. Load the data as above (don't answer from memory for event specifics).
2. Match the user's event name **exactly** when possible; the dataset is
   case-sensitive PascalCase (`ProcessRollup2`, not `process_rollup2`). If the
   user gives an FDR field/event in another casing, search loosely and confirm.
3. Quote the `description` and `platforms` verbatim from the dataset.
4. For "which events…" questions, filter the full list rather than recalling a
   subset, and report counts.
5. Always include a brief caveat: this is an **unofficial** export; verify
   against the official documentation at
   <https://docs.crowdstrike.com/r/en-US/sensormap.ftmap>.

## Caveats

- Unofficial, community-maintained. Not affiliated with or endorsed by
  CrowdStrike, Inc. "CrowdStrike" and "Falcon" are trademarks of CrowdStrike.
- Event definitions are the property of CrowdStrike; reproduced for reference.
- Snapshots are point-in-time. Check the snapshot date and note that newer
  events may exist in the live documentation.
