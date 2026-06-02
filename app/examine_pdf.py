#!/usr/bin/env python3
"""
Helper script to examine PDF structure and test extraction patterns.

Usage:
    uv run app/examine_pdf.py [OPTIONS] [PDF_PATH]
    
Examples:
    uv run app/examine_pdf.py                      # Auto-detect PDF, show first 3 pages
    uv run app/examine_pdf.py -p 10 -n 5           # Show pages 10-14
    uv run app/examine_pdf.py --search "EventName" # Search for pattern
    uv run app/examine_pdf.py custom.pdf -p 100    # Examine page 100 of custom PDF
"""

import argparse
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
    print("  uv run app/examine_pdf.py")
    sys.exit(1)


def examine_pages(pdf_path, start_page=1, num_pages=3):
    """
    Examine a few pages to understand the structure.
    
    Args:
        pdf_path: Path to the PDF file
        start_page: Starting page number (1-indexed)
        num_pages: Number of pages to examine
    """
    if not pdf_path.exists():
        print(f"❌ Error: PDF file not found at {pdf_path}")
        return
    
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        print(f"📄 Total pages in PDF: {total}\n")
        
        # Validate page range
        if start_page < 1 or start_page > total:
            print(f"❌ Error: start_page must be between 1 and {total}")
            return
        
        end_page = min(start_page + num_pages - 1, total)
        
        print(f"Examining pages {start_page} to {end_page}:\n")
        
        for page_num in range(start_page - 1, end_page):
            page = pdf.pages[page_num]
            text = page.extract_text()
            
            print(f"{'='*80}")
            print(f"PAGE {page_num + 1} of {total}")
            print(f"{'='*80}")
            
            if text:
                # Show first 3000 characters
                display_text = text[:3000]
                print(display_text)
                
                if len(text) > 3000:
                    print(f"\n... (truncated, showing first 3000 of {len(text)} characters)\n")
            else:
                print("(No text content extracted from this page)\n")
            
            print()


def search_for_pattern(pdf_path, pattern, max_results=10):
    """
    Search for a specific pattern in the PDF.
    
    Args:
        pdf_path: Path to the PDF file
        pattern: Text pattern to search for
        max_results: Maximum number of results to show
    """
    if not pdf_path.exists():
        print(f"❌ Error: PDF file not found at {pdf_path}")
        return
    
    results = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        print(f"🔍 Searching for '{pattern}' in {total} pages...\n")
        
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if not text:
                continue
            
            if re.search(pattern, text, re.IGNORECASE):
                # Find the context around the pattern
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if re.search(pattern, line, re.IGNORECASE):
                        # Get context (2 lines before and after)
                        start = max(0, i - 2)
                        end = min(len(lines), i + 3)
                        context = '\n'.join(lines[start:end])
                        
                        results.append({
                            'page': page_num,
                            'line': i + 1,
                            'context': context
                        })
                        
                        if len(results) >= max_results:
                            break
            
            if len(results) >= max_results:
                break
        
        # Display results
        if results:
            print(f"✓ Found {len(results)} occurrences:\n")
            for idx, result in enumerate(results, 1):
                print(f"Result {idx} - Page {result['page']}, Line ~{result['line']}:")
                print("-" * 60)
                print(result['context'])
                print("-" * 60)
                print()
        else:
            print("No matches found.")


def find_most_recent_pdf(workspace_root: Path) -> Path | None:
    """
    Find the most recent PDF in ISO-dated directories.

    Searches the ``data/`` subdirectory first, then the workspace root, for
    directories named in ISO 8601 date format (YYYY-MM-DD).

    Args:
        workspace_root: Root directory to search in

    Returns:
        Path to most recent PDF, or None if not found
    """
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

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

    # ISO 8601 dates sort chronologically as plain strings.
    date_dirs.sort(key=lambda d: d.name, reverse=True)

    for date_dir in date_dirs:
        pdf_path = date_dir / "Events Full Reference.pdf"
        if pdf_path.exists():
            return pdf_path

    return None


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Examine CrowdStrike Falcon Events PDF structure.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Show first 3 pages of most recent PDF
  %(prog)s -p 10 -n 5                # Show pages 10-14
  %(prog)s --search "EventName"      # Search for pattern
  %(prog)s custom.pdf -p 100 -n 1    # Show page 100 of custom PDF
        """
    )
    
    parser.add_argument(
        'pdf_path',
        nargs='?',
        type=Path,
        help='Path to PDF file (optional, auto-detects most recent if not provided)'
    )
    
    parser.add_argument(
        '-p', '--page',
        type=int,
        default=1,
        help='Starting page number (default: 1)'
    )
    
    parser.add_argument(
        '-n', '--num-pages',
        type=int,
        default=3,
        help='Number of pages to examine (default: 3)'
    )
    
    parser.add_argument(
        '-s', '--search',
        type=str,
        help='Search for a pattern in the PDF'
    )
    
    parser.add_argument(
        '-m', '--max-results',
        type=int,
        default=10,
        help='Maximum search results to show (default: 10)'
    )
    
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()
    workspace_root = Path(__file__).parent.parent
    
    # Determine PDF path
    if args.pdf_path:
        pdf_path = args.pdf_path if args.pdf_path.is_absolute() else workspace_root / args.pdf_path
    else:
        print("🔍 No PDF specified, searching for most recent version...")
        pdf_path = find_most_recent_pdf(workspace_root)
        
        if not pdf_path:
            print("❌ Error: No PDF found in dated directories.")
            print("\nPlease either:")
            print("  1. Specify a PDF path: uv run app/examine_pdf.py path/to/pdf")
            print("  2. Place PDF in a dated directory (e.g., data/2026-06-02/Events Full Reference.pdf)")
            return
        
        print(f"✓ Found PDF: {pdf_path.relative_to(workspace_root)}\n")
    
    if not pdf_path.exists():
        print(f"❌ Error: PDF file not found at {pdf_path}")
        return
    
    # Execute requested action
    if args.search:
        search_for_pattern(pdf_path, args.search, args.max_results)
    else:
        examine_pages(pdf_path, args.page, args.num_pages)


if __name__ == "__main__":
    main()
