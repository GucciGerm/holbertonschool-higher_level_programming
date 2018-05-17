#!/usr/bin/python3
import sys
import os

"""
Here we will be importing our save_to_json_file and load_from_json_file
and we need to set filename(list) to "add_item.json"
"""

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
filename = "add_item.json"

if __name__ == "__main__":

    pythonlist = []
    if os.path.exists(filename):
        pythonlist = load_from_json_file(filename)
        for n in range(1, len(sys.argv)):
            pythonlist.append(sys.argv[n])
        save_to_json(pythonlist, filename)
