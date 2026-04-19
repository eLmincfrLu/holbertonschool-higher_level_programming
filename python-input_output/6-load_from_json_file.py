#!/usr/bin/python3
"""udsg"""
import json


def load_from_json_file(filename):
    """Fdgfsd"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
