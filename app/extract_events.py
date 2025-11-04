#!/usr/bin/env python3
"""
Extract CrowdStrike Falcon sensor event types from PDF documentation.
Outputs data in both CSV and Markdown formats.

Usage:
    uv run app/extract_events.py [PDF_PATH]
    
    If no PDF path is provided, automatically finds the most recent PDF
    in dated directories (e.g., 10-24-2025/).

Examples:
    uv run app/extract_events.py
    uv run app/extract_events.py path/to/custom.pdf
    uv run app/extract_events.py 10-24-2025/Events\ Full\ Reference.pdf

Requirements:
    - Python 3.10+
    - uv (Python package manager)
    - pdfplumber (automatically installed via uv)
"""

import argparse
import csv
import re
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


def extract_event_data(pdf_path):
    """
    Extract sensor event headers, descriptions, and platforms from PDF.
    
    The expected format in the PDF is:
        EventName
        Description
        Platforms: <platform list>
        <description text>
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        List of dictionaries containing event data
    """
    events = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Processing {total_pages} pages...")
        
        current_header = None
        current_description = []
        current_platforms = []  # Changed to list to collect multiple platform lines
        found_description_keyword = False
        found_platforms = False
        stop_collecting_description = False  # Stop when we hit field definitions
        
        for page_num, page in enumerate(pdf.pages, 1):
            if page_num % 50 == 0:
                print(f"Progress: {page_num}/{total_pages} pages processed ({len(events)} events found)...")
            
            text = page.extract_text()
            if not text:
                continue
            
            lines = text.split('\n')
            
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                i += 1
                
                # Skip empty lines
                if not line:
                    continue
                
                # Pattern 1: Look ahead to see if next line is "Description"
                # This means current line is likely a header (new event starting)
                if i < len(lines) and lines[i].strip() == "Description":
                    # Save any previous event if it's complete (description can be empty)
                    if current_header and current_platforms:
                        description = ' '.join(current_description).strip() if current_description else ''
                        # Combine multiple platform entries
                        platforms_str = ', '.join(current_platforms)
                        events.append({
                            'header': current_header,
                            'description': description,
                            'platforms': platforms_str
                        })
                    
                    # Start new event
                    current_header = line
                    current_description = []
                    current_platforms = []
                    found_description_keyword = False
                    found_platforms = False
                    stop_collecting_description = False
                    continue
                
                # Pattern 2: Look for "Description" keyword
                if line == "Description":
                    found_description_keyword = True
                    continue
                
                # Pattern 3: Look for "Platforms:" line (comes after Description)
                # Can have multiple platform lines, collect them all
                platform_match = re.match(r'^Platforms?:\s*(.+)$', line, re.IGNORECASE)
                if platform_match and found_description_keyword:
                    platform_value = platform_match.group(1).strip()
                    current_platforms.append(platform_value)
                    found_platforms = True
                    continue
                
                # Pattern 4: Collect description text (comes after Platforms line)
                if found_platforms and current_platforms:
                    # Stop collecting if we hit field definitions or other structured content
                    # Common patterns that indicate end of description:
                    # - "Fields:" followed by platform names (e.g., "Fields: Windows, macOS")
                    # - "Field Description" (table header)
                    # - "top [#top]" (end marker)
                    # - CamelCase field names (e.g., "AttemptedActionCount")
                    # - Common field table keywords
                    if (re.match(r'^Fields?:\s+(Windows|macOS|Linux|iOS)', line, re.IGNORECASE) or
                        line.startswith('Field Description') or
                        line.startswith('top [#top]') or
                        line == 'Field' or
                        re.match(r'^(Windows|macOS|Linux|iOS)\s+Field\s+Description', line) or
                        # Detect CamelCase field names (starts with uppercase, has mix of upper/lower, no spaces)
                        # This catches field names like "AttemptedActionCount", "SuccessfulActionCount"
                        (re.match(r'^[A-Z][a-z]+[A-Z][a-zA-Z]*$', line) and 
                         line not in ['Windows', 'Linux', 'macOS', 'iOS']) or
                        # Common field table keywords that appear alone on a line
                        line in ['Values:', 'Value']):
                        # This marks the start of field definitions, stop collecting description
                        stop_collecting_description = True
                        continue
                    
                    # Keep collecting description only if we haven't hit field definitions yet
                    if not stop_collecting_description:
                        current_description.append(line)
                    continue
        
        # Don't forget the last event (description can be empty)
        if current_header and current_platforms:
            description = ' '.join(current_description).strip() if current_description else ''
            # Combine multiple platform entries
            platforms_str = ', '.join(current_platforms)
            events.append({
                'header': current_header,
                'description': description,
                'platforms': platforms_str
            })
    
    print(f"\n✓ Extracted {len(events)} sensor events")
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


def find_most_recent_pdf(workspace_root: Path) -> Path | None:
    """
    Find the most recent PDF in dated directories.
    
    Looks for directories matching date patterns (MM-DD-YYYY) and finds
    PDFs named "Events Full Reference.pdf" within them.
    
    Args:
        workspace_root: Root directory to search in
        
    Returns:
        Path to most recent PDF, or None if not found
    """
    date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    
    # Find all date-formatted directories
    date_dirs = [
        d for d in workspace_root.iterdir()
        if d.is_dir() and date_pattern.match(d.name)
    ]
    
    if not date_dirs:
        return None
    
    # Sort by directory name (which is date) in reverse (most recent first)
    # Format MM-DD-YYYY sorts correctly when comparing strings
    date_dirs.sort(reverse=True)
    
    # Look for PDF in the most recent directory first
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
  %(prog)s 11-04-2025/Events\ Full\ Reference.pdf
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
            print("  2. Place PDF in a dated directory (e.g., 11-04-2025/Events Full Reference.pdf)")
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
