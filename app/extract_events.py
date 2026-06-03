#!/usr/bin/env python3
"""
Extract CrowdStrike Falcon sensor event types from PDF documentation.
Outputs data in both CSV and Markdown formats.

Usage:
    uv run app/extract_events.py [PDF_PATH]
    
    If no PDF path is provided, automatically finds the most recent PDF
    in ISO-dated directories (e.g., data/2026-06-02/).

Examples:
    uv run app/extract_events.py
    uv run app/extract_events.py path/to/custom.pdf
    uv run app/extract_events.py data/2026-06-02/Events\ Full\ Reference.pdf

Requirements:
    - Python 3.10+
    - uv (Python package manager)
    - pdfplumber (automatically installed via uv)
"""

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("\n❌ Error: pdfplumber is not installed.")
    print("\nPlease install it using uv:")
    print("  uv sync")
    print("\nOr run the script with uv:")
    print("  uv run app/extract_events.py")
    sys.exit(1)


# Known sensor platforms. Used to detect when a "Platforms:" value wraps
# across several lines so the full list is captured.
PLATFORM_TOKENS = {
    "Windows",
    "Windows Legacy",
    "Linux",
    "macOS",
    "iOS",
    "Android",
    "ChromeOS",
    "Falcon Container",
    "Forensics",
    "Kubernetes",
    "Vmcluster",
    "Public Cloud",
}

# Lines that are page furniture (running headers/footers) rather than content.
_NOISE_EXACT = {"Sensor Events", "Field Description", "Copyright © CrowdStrike"}
_PAGE_FOOTER_RE = re.compile(r"^Page \d+ of \d+$")
_DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")
_TOC_ENTRY_RE = re.compile(r"^(\d+)\.([A-Za-z][A-Za-z0-9]*)$")
_EVENT_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")


def _is_platform_line(line: str) -> bool:
    """Return True if a line consists solely of known platform tokens."""
    parts = [p.strip() for p in line.split(",") if p.strip()]
    return bool(parts) and all(p in PLATFORM_TOKENS for p in parts)


def _read_toc(pdf) -> list[str]:
    """Read the numbered table of contents to get the authoritative event list.

    The reference PDF opens with a numbered index of every event, e.g.
    ``1.AbnormalTerminationNotification``. We use this both as a whitelist of
    valid event names and to validate the final extraction count.
    """
    names: list[str] = []
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue
        page_hits = 0
        for line in text.split("\n"):
            match = _TOC_ENTRY_RE.match(line.strip())
            if match:
                names.append(match.group(2))
                page_hits += 1
        # The TOC is contiguous at the front of the document. Once we hit a
        # content page with no numbered entries (after starting), stop.
        if names and page_hits == 0:
            break
    return names


def extract_event_data(pdf_path):
    """Extract sensor event headers, descriptions, and platforms from the PDF.

    The 2026 reference layout repeats each event title on two consecutive
    lines, followed by its platforms and an optional description::

        AccessoryDisconnected
        AccessoryDisconnected
        Platforms: Android, iOS
        Sent when a device disconnects from an external accessory...
        Fields: Android
        Field Description
        <field rows>

    Args:
        pdf_path: Path to the PDF file

    Returns:
        List of dictionaries containing event data (header, description,
        platforms), in document (alphabetical) order.
    """
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Processing {total_pages} pages...")

        toc_names = _read_toc(pdf)
        toc_set = set(toc_names)
        if toc_names:
            print(f"Table of contents lists {len(toc_names)} events.")

        # Flatten the document into a single list of content lines, dropping
        # page furniture so an event title split across a page break becomes
        # adjacent again.
        lines: list[str] = []
        for page_num, page in enumerate(pdf.pages, 1):
            if page_num % 200 == 0:
                print(f"Progress: {page_num}/{total_pages} pages read...")
            text = page.extract_text()
            if not text:
                continue
            for raw in text.split("\n"):
                line = raw.strip()
                if not line:
                    continue
                if line in _NOISE_EXACT or _PAGE_FOOTER_RE.match(line) or _DATE_RE.match(line):
                    continue
                if _TOC_ENTRY_RE.match(line):
                    continue
                lines.append(line)

    events = []
    seen = set()
    n = len(lines)
    i = 0
    while i < n - 2:
        header = lines[i]
        # An event starts where its title appears twice in a row and is
        # immediately followed by a "Platforms:" line.
        is_header = (
            _EVENT_NAME_RE.match(header)
            and lines[i + 1] == header
            and lines[i + 2].startswith("Platforms:")
            and (not toc_set or header in toc_set)
        )
        if not is_header or header in seen:
            i += 1
            continue

        seen.add(header)

        # Capture platforms, allowing the list to wrap onto following lines.
        platforms = lines[i + 2][len("Platforms:"):].strip()
        j = i + 3
        while j < n and _is_platform_line(lines[j]) and not lines[j].startswith("Fields:"):
            platforms += ", " + lines[j]
            j += 1

        # Capture the optional free-text description until the field tables
        # begin ("Fields:") or the next event starts.
        description_parts = []
        while j < n:
            line = lines[j]
            if line.startswith("Fields:"):
                break
            # Next event header reached without a Fields section.
            if (
                line in toc_set
                and j + 1 < n
                and lines[j + 1] == line
                and j + 2 < n
                and lines[j + 2].startswith("Platforms:")
            ):
                break
            description_parts.append(line)
            j += 1

        events.append({
            "header": header,
            "description": " ".join(description_parts).strip(),
            "platforms": platforms,
        })
        i = j

    print(f"\n✓ Extracted {len(events)} sensor events")
    if toc_names:
        missing = [name for name in toc_names if name not in seen]
        if missing:
            preview = ", ".join(missing[:10])
            more = "" if len(missing) <= 10 else f" (+{len(missing) - 10} more)"
            print(f"⚠️  {len(missing)} TOC events not matched: {preview}{more}")
        else:
            print("✓ All table-of-contents events were extracted.")
    return events


def save_to_csv(events, output_path):
    """Save events data to CSV file."""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['header', 'description', 'platforms'])
        writer.writeheader()
        writer.writerows(events)
    print(f"✓ CSV saved to: {output_path}")


def save_to_markdown(events, output_path):
    """Save events data to Markdown file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        # Write header
        f.write("# CrowdStrike Falcon Sensor Events\n\n")
        f.write(f"**Total Events:** {len(events)}\n\n")
        f.write("---\n\n")
        
        # Write table of contents
        f.write("## Table of Contents\n\n")
        for event in events:
            anchor = event['header'].lower().replace(' ', '-')
            f.write(f"- [{event['header']}](#{anchor})\n")
        f.write("\n---\n\n")
        
        # Write summary table
        f.write("## Summary Table\n\n")
        f.write("| Header | Description | Platforms |\n")
        f.write("|--------|-------------|------------|\n")
        
        for event in events:
            header = event['header'].replace('|', '\\|')
            # Truncate long descriptions for table
            description = event['description'][:100] + '...' if len(event['description']) > 100 else event['description']
            description = description.replace('|', '\\|').replace('\n', ' ')
            platforms = event['platforms'].replace('|', '\\|')
            f.write(f"| {header} | {description} | {platforms} |\n")
        
        # Write detailed section
        f.write("\n\n## Detailed Event Information\n\n")
        for event in events:
            anchor = event['header'].lower().replace(' ', '-')
            f.write(f"### {event['header']}\n\n")
            f.write(f"**Description:** {event['description']}\n\n")
            f.write(f"**Platforms:** {event['platforms']}\n\n")
            f.write("---\n\n")
    
    print(f"✓ Markdown saved to: {output_path}")


_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def iso_date_dirs(workspace_root: Path) -> list[Path]:
    """Return ISO-dated snapshot directories under ``data/``, newest first."""
    data_dir = workspace_root / "data"
    if not data_dir.is_dir():
        return []
    dirs = [
        d for d in data_dir.iterdir()
        if d.is_dir() and _ISO_DATE_RE.match(d.name)
    ]
    # ISO 8601 dates sort chronologically as plain strings.
    dirs.sort(key=lambda d: d.name, reverse=True)
    return dirs


def update_current_snapshot(workspace_root: Path, csv_path: Path,
                            md_path: Path, date_str: str) -> None:
    """Mirror the newest snapshot into ``data/current/`` for stable raw URLs.

    External consumers (RAG pipelines, SIEMs) can point at ``data/current/``
    and always get the latest export without the URL changing each release.
    """
    current = workspace_root / "data" / "current"
    current.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(csv_path, current / "sensor_events.csv")
    shutil.copyfile(md_path, current / "sensor_events.md")
    (current / "SOURCE.md").write_text(
        "# data/current\n\n"
        "This folder is **auto-generated** by `app/extract_events.py`. It always\n"
        "mirrors the newest dated snapshot so external tools can rely on stable,\n"
        "unchanging raw URLs.\n\n"
        f"- Mirrors: [`data/{date_str}/`](../{date_str}/)\n"
        "- Regenerated whenever the newest snapshot is (re-)extracted.\n\n"
        "**Do not edit these files by hand.** If you need a fixed version, link to\n"
        "the dated folder instead of this one.\n",
        encoding="utf-8",
    )
    print(f"✓ data/current/ synced from {date_str}")


def _shields_escape(text: str) -> str:
    """Escape a string for a shields.io badge (single dashes are separators)."""
    return text.replace("-", "--")


def _replace_marked_block(text: str, name: str, transform) -> tuple[str, int]:
    """Apply ``transform`` to the content between ``<!-- NAME:START ... -->`` and
    ``<!-- NAME:END -->`` markers, leaving the markers themselves intact."""
    pattern = re.compile(
        rf"(<!--\s*{name}:START.*?-->)(.*?)(<!--\s*{name}:END\s*-->)",
        re.DOTALL,
    )
    return pattern.subn(
        lambda m: m.group(1) + transform(m.group(2)) + m.group(3),
        text,
    )


def update_readme(readme_path: Path, date_str: str, count: int) -> None:
    """Refresh the auto-updated badge/snapshot regions of the README in place."""
    if not readme_path.exists():
        return
    text = original = readme_path.read_text(encoding="utf-8")

    def _badges(block: str) -> str:
        block = re.sub(r"events-\d[\d,]*-", f"events-{count}-", block)
        block = re.sub(
            r"data-\d{4}--\d{2}--\d{2}-",
            f"data-{_shields_escape(date_str)}-",
            block,
        )
        return block

    def _latest(block: str) -> str:
        block = re.sub(r"data/\d{4}-\d{2}-\d{2}", f"data/{date_str}", block)
        block = re.sub(
            r"\d[\d,]* sensor events", f"{count} sensor events", block
        )
        return block

    text, nb = _replace_marked_block(text, "BADGES", _badges)
    text, nl = _replace_marked_block(text, "LATEST", _latest)

    if text != original:
        readme_path.write_text(text, encoding="utf-8")
        print(f"✓ README.md refreshed → {date_str}, {count} events")
    else:
        print("• README.md already current.")


def update_llms(llms_path: Path, date_str: str, count: int) -> None:
    """Refresh the dated/count references in ``llms.txt`` in place."""
    if not llms_path.exists():
        return
    text = original = llms_path.read_text(encoding="utf-8")
    text = re.sub(r"latest:\s*\d{4}-\d{2}-\d{2}", f"latest: {date_str}", text)
    text = re.sub(r"documents \d[\d,]* events", f"documents {count} events", text)
    text = re.sub(r"All \d[\d,]* events", f"All {count} events", text)
    if text != original:
        llms_path.write_text(text, encoding="utf-8")
        print(f"✓ llms.txt refreshed → {date_str}, {count} events")
    else:
        print("• llms.txt already current.")


def update_skill(skill_path: Path, count: int) -> None:
    """Refresh the event count referenced in the Claude Skill markdown."""
    if not skill_path.exists():
        return
    text = original = skill_path.read_text(encoding="utf-8")
    text = re.sub(r"dictionary of \d[\d,]* events",
                  f"dictionary of {count} events", text)
    text = re.sub(r"\d[\d,]* CrowdStrike Falcon sensor events",
                  f"{count} CrowdStrike Falcon sensor events", text)
    if text != original:
        skill_path.write_text(text, encoding="utf-8")
        print(f"✓ SKILL.md refreshed → {count} events")
    else:
        print("• SKILL.md already current.")


def update_prompt(prompt_path: Path, count: int) -> None:
    """Refresh the event count referenced in the copy-paste system prompt."""
    if not prompt_path.exists():
        return
    text = original = prompt_path.read_text(encoding="utf-8")
    text = re.sub(r"export of \d[\d,]* events", f"export of {count} events", text)
    if text != original:
        prompt_path.write_text(text, encoding="utf-8")
        print(f"✓ system-prompt.md refreshed → {count} events")
    else:
        print("• system-prompt.md already current.")


def find_most_recent_pdf(workspace_root: Path) -> Path | None:
    """
    Find the most recent PDF in ISO-dated directories.

    Looks for directories named in ISO 8601 date format (YYYY-MM-DD) and
    finds PDFs named "Events Full Reference.pdf" within them. Both the
    ``data/`` subdirectory and the workspace root are searched, so datasets
    can live under ``data/2026-06-02/`` (preferred) or directly at the root.

    Args:
        workspace_root: Root directory to search in

    Returns:
        Path to most recent PDF, or None if not found
    """
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Search the dedicated data/ directory first, then the workspace root.
    search_roots = [workspace_root / "data", workspace_root]

    date_dirs = []
    for root in search_roots:
        if not root.is_dir():
            continue
        date_dirs.extend(
            d for d in root.iterdir()
            if d.is_dir() and date_pattern.match(d.name)
        )

    if not date_dirs:
        return None

    # Sort by directory name (the ISO date) in reverse (most recent first).
    # ISO 8601 dates sort chronologically as plain strings.
    date_dirs.sort(key=lambda d: d.name, reverse=True)

    # Look for the PDF in the most recent directory first.
    for date_dir in date_dirs:
        pdf_path = date_dir / "Events Full Reference.pdf"
        if pdf_path.exists():
            return pdf_path

    return None


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Extract CrowdStrike Falcon sensor events from PDF documentation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Auto-detect most recent PDF
  %(prog)s data/2026-06-02/Events\ Full\ Reference.pdf
  %(prog)s /path/to/custom.pdf
        """
    )
    
    parser.add_argument(
        'pdf_path',
        nargs='?',
        type=Path,
        help='Path to the PDF file. If not provided, searches for most recent PDF.'
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        type=Path,
        help='Output directory for CSV and Markdown files (default: same as PDF directory)'
    )
    
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()
    workspace_root = Path(__file__).parent.parent
    
    # Determine PDF path
    if args.pdf_path:
        # Use provided path (resolve relative to workspace root if relative)
        pdf_path = args.pdf_path if args.pdf_path.is_absolute() else workspace_root / args.pdf_path
    else:
        # Auto-detect most recent PDF
        print("🔍 No PDF specified, searching for most recent version...")
        pdf_path = find_most_recent_pdf(workspace_root)
        
        if not pdf_path:
            print("❌ Error: No PDF found in dated directories.")
            print("\nPlease either:")
            print("  1. Specify a PDF path: uv run app/extract_events.py path/to/pdf")
            print("  2. Place PDF in a dated directory (e.g., data/2026-06-02/Events Full Reference.pdf)")
            return 1
        
        print(f"✓ Found PDF: {pdf_path.relative_to(workspace_root)}\n")
    
    # Verify PDF exists
    if not pdf_path.exists():
        print(f"❌ Error: PDF file not found at {pdf_path}")
        return 1
    
    # Determine output directory
    output_dir = args.output_dir if args.output_dir else pdf_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    csv_output = output_dir / "sensor_events.csv"
    md_output = output_dir / "sensor_events.md"
    
    print(f"📄 Reading PDF: {pdf_path}\n")
    
    # Extract event data
    try:
        events = extract_event_data(pdf_path)
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    if not events:
        print("⚠️  Warning: No events were extracted. Please check the PDF format.")
        return 1
    
    # Save to CSV
    try:
        save_to_csv(events, csv_output)
    except Exception as e:
        print(f"❌ Error saving CSV: {e}")
        return 1
    
    # Save to Markdown
    try:
        save_to_markdown(events, md_output)
    except Exception as e:
        print(f"❌ Error saving Markdown: {e}")
        return 1

    # Keep data/current/ and the docs in sync — but only when we just generated
    # the newest dated snapshot, so re-running an old export can't clobber the
    # "current" pointer (or the README) with stale data.
    snapshot_date = None
    if _ISO_DATE_RE.match(output_dir.name):
        date_dirs = iso_date_dirs(workspace_root)
        if date_dirs and output_dir.resolve() == date_dirs[0].resolve():
            snapshot_date = output_dir.name

    if snapshot_date:
        try:
            update_current_snapshot(workspace_root, csv_output, md_output, snapshot_date)
            update_readme(workspace_root / "README.md", snapshot_date, len(events))
            update_llms(workspace_root / "llms.txt", snapshot_date, len(events))
            update_skill(
                workspace_root / "skills" / "crowdstrike-falcon-events" / "SKILL.md",
                len(events),
            )
            update_prompt(
                workspace_root / "prompts" / "system-prompt.md", len(events)
            )
        except Exception as e:
            print(f"⚠️  Could not refresh data/current/ or docs: {e}")
    else:
        print("• Skipped data/current/ + docs refresh (not the newest dated snapshot).")

    print("\n" + "="*60)
    print("✅ Extraction complete!")
    print("="*60)
    print(f"  📊 Events extracted: {len(events)}")
    print(f"  📄 CSV output: {csv_output}")
    print(f"  📝 Markdown output: {md_output}")
    print("="*60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
