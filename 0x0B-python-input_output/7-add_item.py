#!/usr/bin/python3
import sys
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
try:
    args = load('add_item.json')
except Exception:
    args = []
args.extend([sys.argv[i] for i in range(len(sys.argv)) if i > 0])
save(args, 'add_item.json')
