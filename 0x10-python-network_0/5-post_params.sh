#!/bin/bash
#This script sends a post request with variables to a server
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
