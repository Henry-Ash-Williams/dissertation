#!/bin/bash

pnpm dev --target=firefox-mv2 
cd build/firefox-mv2-dev
web-ext build 
web-ext --bc -f '/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox-bin' run
