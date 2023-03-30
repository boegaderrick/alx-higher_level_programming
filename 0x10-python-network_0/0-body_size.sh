#!/bin/bash
#This script curls a URL and displays body size only
curl -s -w "%{size_download}"'\n' "$1" -o /tmp/temp
