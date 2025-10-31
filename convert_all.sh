#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

CSS_SIZE=75     # ← set this to the CSS px you actually use
OUT=converted; mkdir -p "$OUT"

build_svg() {
  local f="$1" base="${f##*/}"; base="${base%.*}"
  magick -background none "$f" -alpha set -strip -filter Lanczos -resize ${CSS_SIZE}x \
    -define webp:lossless=true -define webp:exact=true "$OUT/${base}@1x.webp"
  magick -background none "$f" -alpha set -strip -filter Lanczos -resize $((CSS_SIZE*2))x \
    -define webp:lossless=true -define webp:exact=true "$OUT/${base}@2x.webp"
}
build_png() {
  local f="$1" base="${f##*/}"; base="${base%.*}"
  magick "$f" -strip -filter Lanczos -resize ${CSS_SIZE}x\> \
    -define webp:lossless=true -define webp:exact=true "$OUT/${base}@1x.webp"
  magick "$f" -strip -filter Lanczos -resize $((CSS_SIZE*2))x\> \
    -define webp:lossless=true -define webp:exact=true "$OUT/${base}@2x.webp"
}

for f in assets/*.svg; do build_svg "$f"; done
for f in assets/*.png; do build_png "$f"; done
