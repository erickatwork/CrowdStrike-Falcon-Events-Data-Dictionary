# CrowdStrike-Falcon-Events-Data-Dictionary

This repository contains CrowdStrike Falcon Events documentation and tools to extract sensor event data from PDF documentation.

The data dictionary is available at: https://falcon.crowdstrike.com/documentation/page/e3ce0b24/events-data-dictionary

I'm sharing it here as it's behind auth, and I wanted to share it with the community. The document is also huge so its very hard to navigate. I created this tool to help me extract the primary info I needed.

## 📁 Contents

- **PDF Documentation**: CrowdStrike Falcon Events Full Reference documentation
- **Extraction Tools**: Python scripts to extract sensor events data from the PDF
- **Output Formats**: CSV and Markdown exports of sensor event information

## 🚀 Quick Start

Extract all sensor events from the PDF documentation:

```bash
# 1. Install uv (if not already installed)
# See https://docs.astral.sh/uv/getting-started/installation/
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or use pip: pip install uv

# 2. Place your PDF in a dated directory (e.g., 11-04-2025/Events Full Reference.pdf)

# 3. Run extraction (auto-detects most recent PDF)
uv run app/extract_events.py

# Or specify a custom PDF path:
uv run app/extract_events.py path/to/custom.pdf
```

This will generate (in the same directory as the PDF):
- `sensor_events.csv` - All events in CSV format
- `sensor_events.md` - All events in Markdown format with table of contents

## 🛠 Tools Included

### extract_events.py
Main extraction script that reads the PDF and extracts:
- Event headers/names
- Event descriptions
- Supported platforms

**Features:**
- Auto-detects most recent PDF in dated directories
- Accepts custom PDF paths
- Outputs to same directory as PDF by default
- Optional custom output directory

**Usage:**
```bash
# Auto-detect most recent PDF
uv run app/extract_events.py

# Use specific PDF
uv run app/extract_events.py 11-04-2025/Events\ Full\ Reference.pdf

# Custom output directory
uv run app/extract_events.py -o output/
```

### examine_pdf.py
Helper script to examine PDF structure and search for patterns.

**Usage:**
```bash
# View first 3 pages (auto-detects PDF)
uv run app/examine_pdf.py

# View specific pages
uv run app/examine_pdf.py -p 10 -n 5  # Pages 10-14

# Search for patterns
uv run app/examine_pdf.py --search "EventName"

# Use custom PDF
uv run app/examine_pdf.py custom.pdf -p 100 -n 1
```

## 📊 Output Format

### CSV Output
```csv
header,description,platforms
HookedDriverObject,"This event tracks...",Windows
AnotherEvent,"Description here","Windows, Mac, Linux"
```

### Markdown Output
- Table of contents with links to each event
- Summary table
- Detailed sections for each event

## 🔧 Requirements

- Python 3.10+
- uv (Python package manager)
- pdfplumber (automatically installed via uv)

## 📝 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📚 Resources

- [CrowdStrike Falcon Documentation](https://www.crowdstrike.com/)
- [Official Events Data Dictionary](https://falcon.crowdstrike.com/documentation/page/e3ce0b24/events-data-dictionary) (requires authentication)
- Latest Events Reference PDF in `10-24-2025/` directory
- [uv Documentation](https://docs.astral.sh/uv/)
