#!/usr/bin/python3
"""
Script for adding command line arguments,
to a Python list and saving them to a JSON file.
"""
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except Exception:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, filename)
