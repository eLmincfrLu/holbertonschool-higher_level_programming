#!/usr/bin/python3
"""aadsd"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


file = "add_item.json"
try:
    items = load_from_json_file(file)
except Exception:
      items = []
for i in sys.argv[1:]:
        items.append(i)
save_to_json_file(items, file)
