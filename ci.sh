#!/bin/bash -ex
HUGO_VERSION='0.120.4'

echo 'Downloading Hugo...'
wget -q "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
sudo dpkg -i "hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
