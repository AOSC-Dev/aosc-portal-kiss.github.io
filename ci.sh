#!/bin/bash -e
HUGO_VERSION='0.68.3'

echo 'Downloading Hugo...'
wget -q "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.deb"
sudo dpkg -i "hugo_extended_${HUGO_VERSION}_Linux-64bit.deb"
