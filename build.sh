#!/bin/bash -e
TOPDIR=$(dirname "${BASH_SOURCE[0]}")
# generate thumbnails
function generateDEThumbnails() {
    convert "$1" -resize 960x540 -quality 87 "$2"
    echo "$1 -> $2"
}

echo 'Generating thumbnails...'

for i in "${TOPDIR}/static/img/de-preview"/**/*.png; do
    mkdir -p "$(dirname $i)/thumbs/"
    generateDEThumbnails "${i}" "$(dirname $i)/thumbs/$(basename $i).jpg"
done

echo -e '\n... Done'

echo 'Generating HTML files...'

hugo --cleanDestinationDir

echo '... Done'
