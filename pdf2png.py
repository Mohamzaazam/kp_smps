#!/usr/bin/env python3
"""
PDF to PNG Converter
Extracts pages from a PDF file as high-resolution PNG images.

Requirements:
    pip install pdf2image
    
    You also need poppler installed:
    - macOS: brew install poppler
    - Ubuntu/Debian: sudo apt-get install poppler-utils
    - Windows: Download from https://github.com/osber/poppler-for-windows/releases
               and add the bin/ folder to your PATH
"""

import argparse
import os
from pathlib import Path
from pdf2image import convert_from_path, pdfinfo_from_path


def pdf_to_png(
    pdf_path: str,
    output_dir: str = None,
    dpi: int = 300,
    start_page: int = None,
    end_page: int = None,
    prefix: str = None
):
    """
    Convert PDF pages to high-resolution PNG images.
    
    Args:
        pdf_path: Path to the input PDF file
        output_dir: Directory to save PNG files (default: same as PDF)
        dpi: Resolution in dots per inch (default: 300)
        start_page: First page to convert (1-indexed, default: 1)
        end_page: Last page to convert (1-indexed, default: last page)
        prefix: Prefix for output filenames (default: PDF filename)
    
    Returns:
        List of paths to the generated PNG files
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Get PDF info
    info = pdfinfo_from_path(str(pdf_path))
    total_pages = info["Pages"]
    
    # Set defaults
    if output_dir is None:
        output_dir = pdf_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    if start_page is None:
        start_page = 1
    if end_page is None:
        end_page = total_pages
    if prefix is None:
        prefix = pdf_path.stem
    
    # Validate page range
    if start_page < 1:
        raise ValueError("start_page must be >= 1")
    if end_page > total_pages:
        raise ValueError(f"end_page ({end_page}) exceeds total pages ({total_pages})")
    if start_page > end_page:
        raise ValueError("start_page must be <= end_page")
    
    print(f"PDF: {pdf_path.name}")
    print(f"Total pages: {total_pages}")
    print(f"Converting pages {start_page} to {end_page} at {dpi} DPI")
    print(f"Output directory: {output_dir}")
    print("-" * 40)
    
    # Convert PDF to images
    images = convert_from_path(
        str(pdf_path),
        dpi=dpi,
        first_page=start_page,
        last_page=end_page
    )
    
    # Save images
    output_paths = []
    for i, image in enumerate(images):
        page_num = start_page + i
        output_filename = f"{prefix}_page_{page_num:04d}.png"
        output_path = output_dir / output_filename
        
        image.save(str(output_path), "PNG")
        output_paths.append(output_path)
        print(f"Saved: {output_filename}")
    
    print("-" * 40)
    print(f"Done! Extracted {len(output_paths)} page(s)")
    
    return output_paths


def main():
    parser = argparse.ArgumentParser(
        description="Extract PDF pages as high-resolution PNG images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert all pages at 300 DPI
  python pdf_to_png.py document.pdf

  # Convert pages 5-10 at 600 DPI
  python pdf_to_png.py document.pdf --start 5 --end 10 --dpi 600

  # Convert to specific output directory
  python pdf_to_png.py document.pdf --output ./images

  # Convert with custom filename prefix
  python pdf_to_png.py document.pdf --prefix chapter1
        """
    )
    
    parser.add_argument("pdf", help="Path to the input PDF file")
    parser.add_argument("-o", "--output", default="extracted", help="Output directory (default: extracted)")
    parser.add_argument("-d", "--dpi", type=int, default=300,
                        help="Resolution in DPI (default: 300)")
    parser.add_argument("-s", "--start", type=int, default=None,
                        help="Start page (1-indexed, default: 1)")
    parser.add_argument("-e", "--end", type=int, default=None,
                        help="End page (1-indexed, default: last page)")
    parser.add_argument("-p", "--prefix", default=None,
                        help="Output filename prefix (default: PDF filename)")
    
    args = parser.parse_args()
    
    try:
        pdf_to_png(
            pdf_path=args.pdf,
            output_dir=args.output,
            dpi=args.dpi,
            start_page=args.start,
            end_page=args.end,
            prefix=args.prefix
        )
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())