#!/usr/bin/python3
"""dfghjkl"""
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csvf:
            data = list(csv.DictReader(csv_filename))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except FileNotFoundError:
        return False
