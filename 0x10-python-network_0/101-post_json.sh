#!/bin/bash
#This script posts a json file
curl -s -d @"$2" -H "Content-Type: application/json" "$1"
