#!/bin/bash

# Create dev build 
pnpm dev --target=firefox-mv2 &
# Enter build directory 
cd build/firefox-mv2-dev
# Build using web-ext 
web-ext build 
# Load firefox with extension running
web-ext --bc -f '/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox-bin' run
# Enter previous directory 
cd -