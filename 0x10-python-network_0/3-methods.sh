#!/bin/bash
#This script displays allowed methods of a url
curl -s -I "$1" | grep "Allow" | awk '{for (i=2; i<=NF; i++) if ($i==$2) {printf"%s",$i} else {printf" %s",$i}} END {printf"\n"}'
