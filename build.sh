#!/bin/bash -e
TOPDIR=$(dirname "${BASH_SOURCE[0]}")
# generate thumbnails
function generateDEThumbnails() {
    convert "$1" -resize 960x540 -quality 87 "$2"
    echo "$1 -> $2"
}

echo 'Generating thumbnails...'

for i in "${TOPDIR}/assets/img/de-preview"/**/*.png; do
    mkdir -p "$(dirname $i)/thumbs/"
    generateDEThumbnails "${i}" "$(dirname $i)/thumbs/$(basename $i).jpg"
done

echo -e '\n... Done'

echo 'Generating HTML files...'

if command -v jekyll >/dev/null; then
    JEKYLL_BIN='jekyll'
elif bundle exec jekyll -v >/dev/null; then
    JEKYLL_BIN='bundle exec jekyll'
else
    bundle install --path vendor/bundle
    JEKYLL_BIN='bundle exec jekyll'
fi

$JEKYLL_BIN build

echo '... Done'
