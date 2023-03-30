#!/bin/bash
#This script sends a request and display the status code returned
curl -s -w "%{response_code}" "$1" -o /tmp/temp
