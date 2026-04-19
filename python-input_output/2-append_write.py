#!/usr/bin/python3
"""fd"""


def append_write(filename="", text=""):
    """frg"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
