#!/usr/bin/python3
"""sdghjkl"""
import json

def serialize_and_save_to_file(data, filename):
    """dfghjkl"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """fghjkl"""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
