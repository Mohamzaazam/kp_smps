#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

OUTDIR="converted"
mkdir -p "$OUTDIR"

# SVGs
for f in assets/*.svg; do
  b="${f##*/}"; n="${b%.svg}"
  magick "$f" -background none -alpha on -strip png:- | cwebp -lossless -exact - -o "$OUTDIR/$n.webp"
done

# PNGs
for f in assets/*.png; do
  b="${f##*/}"; n="${b%.png}"
  cwebp -lossless -exact "$f" -o "$OUTDIR/$n.webp"
done
