# KP Links & PDF-to-PNG Extractor

Social-media link page for **Khair Publications**, plus a utility to extract PDF pages as high-resolution PNG images.

---

## Prerequisites

### 1. Install system tools (one-time)

```powershell
# Pixi (package manager) — installs Python + poppler automatically
winget install -e --id prefix-dev.pixi

# Only needed for the SVG/WebP asset pipeline (optional)
winget install -e --id ImageMagick.ImageMagick
winget install -e --id Google.Libwebp
winget install -e --id Inkscape.Inkscape
```

> **Note:** After installing, fully quit and relaunch VS Code so it picks up PATH changes.
> If the terminal still can't find the tools, refresh PATH manually:
>
> ```powershell
> $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' +
>             [Environment]::GetEnvironmentVariable('Path','User')
> ```

### 2. Install project dependencies

```powershell
cd path\to\kp_smps
pixi install          # creates .pixi env with Python 3.12 + pdf2image + poppler
```

---

## PDF → PNG Extraction

### Quick start

```powershell
# Extract ALL pages at 300 DPI (default) into extracted/
pixi run python pdf2png.py <your-file>.pdf

# Extract specific page range
pixi run python pdf2png.py <your-file>.pdf --start 1 --end 50

# Custom output directory and DPI
pixi run python pdf2png.py <your-file>.pdf --output ./my_images --dpi 600
```

### Full CLI reference

```
usage: pdf2png.py [-h] [-o OUTPUT] [-d DPI] [-s START] [-e END] [-p PREFIX] pdf

Extract PDF pages as high-resolution PNG images.

positional arguments:
  pdf                   Path to the input PDF file

options:
  -o, --output OUTPUT   Output directory (default: extracted)
  -d, --dpi DPI         Resolution in DPI (default: 300)
  -s, --start START     Start page, 1-indexed (default: first page)
  -e, --end END         End page, 1-indexed (default: last page)
  -p, --prefix PREFIX   Output filename prefix (default: PDF filename)
```

### Output format

Files are saved as `page_NNNN.png` (e.g., `page_0001.png`, `page_0042.png`).

### Large PDFs

For PDFs with many pages, process in batches to limit memory usage:

```powershell
pixi run python pdf2png.py big_book.pdf -s 1 -e 30
pixi run python pdf2png.py big_book.pdf -s 31 -e 60
# ... and so on
```

---

## SVG / WebP Asset Pipeline (optional)

Convert SVG and PNG assets in `assets/` to optimised WebP files for the link page:

```bash
bash convert_all.sh
```

Requires ImageMagick, libwebp, and Inkscape (see Prerequisites).

### Verify tool versions

```powershell
magick -version
cwebp -version
inkscape --version            # use inkscape.com on Windows for console output
```

> **Windows tip:** `inkscape.com` is the console binary; `inkscape.exe` is GUI-only.
> Add an alias if needed:
>
> ```powershell
> Set-Alias inkscape 'C:\Program Files\Inkscape\bin\inkscape.com'
> ```

---

## Project Structure

```
kp_smps/
├── index.html          # Social-media link page
├── pdf2png.py          # PDF → PNG extraction script
├── convert_all.sh      # SVG/PNG → WebP asset converter
├── pixi.toml           # Pixi environment config
├── assets/             # Source SVG/PNG assets
├── converted/          # Generated WebP assets
└── extracted/          # Extracted PDF page images (gitignored)
```
