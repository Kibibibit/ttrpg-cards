#!/bin/bash
wkhtmltopdf \
    --enable-local-file-access \
    -B 0 -L 0 -R 0 -T 0 \
    -d 300 \
    --disable-smart-shrinking \
    --page-width 76mm \
    --page-height 101mm \
    --debug-javascript \
    --allow ./index.js \
    --encoding utf-8 \
    --no-outline \
    index.html \
    out.pdf