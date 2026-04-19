#!/usr/bin/python3
"""gdzjdzs"""
import json


def load_from_json_file(filename):
    """sdd"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
