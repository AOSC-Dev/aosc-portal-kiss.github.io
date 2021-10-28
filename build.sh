#!/bin/bash -e
echo 'Generating HTML files...'

hugo --cleanDestinationDir --gc

echo '... Done'
