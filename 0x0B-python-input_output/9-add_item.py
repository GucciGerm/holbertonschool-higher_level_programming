#!/usr/bin/python3
from sys import argv
"""
Here we will be importing our save_to_json_file and load_from_json_file
"""

save_to_json_file = __import__("7-save_to_json_file").7-save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").8-load_from_json_file

try:
    load = load_from_json_file("8-load_from_json_file")

except:
    load = []

    for n, count in enumerate(argv):
        if n > 0:
            load.append(count)
    save_to_json(text, "add_item.json")
