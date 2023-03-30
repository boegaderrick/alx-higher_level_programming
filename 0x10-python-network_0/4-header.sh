#!/bin/bash
#This script sends a header variable to the url passed as argument
curl -s -H "X-School-User_Id: 98" "$1"
