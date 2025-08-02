# PDF 4-Up Tight Layout Tool

A Python script to convert a PDF into a compact 4-page-per-sheet layout with minimal margins, perfect for printing or space-optimized document viewing.

 

## Features ✨
- Converts single-page PDFs into space-efficient 4-up layouts
- Precise margin control (adjustable outer and gutter margins)
- Maintains original image quality (150 DPI default)
- Lightweight PDF processing using ReportLab and pdf2image

## Installation 🛠️

### Prerequisites
- Python 3.6+
- Poppler utilities (for pdf2image)

```bash
# On Ubuntu/Debian:
sudo apt install poppler-utils

# On macOS (using Homebrew):
brew install poppler
pip install reportlab pdf2image

#Usage 🚀
from pdf_4up_converter import pdf_4_pages_tight_layout

# Basic usage:
pdf_4_pages_tight_layout("input.pdf", "output.pdf")

# Advanced usage with custom margins:
pdf_4_pages_tight_layout(
    input_pdf_path="document.pdf",
    output_pdf_path="compact_output.pdf",
    dpi=300,               # Higher quality
    outer_margin=1.5,      # cm
    gutter_margin=0.2      # cm between pages
)
git clone https://github.com/yourusername/pdf-4up-tight-layout.git
cd pdf-4up-tight-layout
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -e .