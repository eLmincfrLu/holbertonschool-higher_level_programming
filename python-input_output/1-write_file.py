#!/usr/bin/python3
"""fghjk"""


def write_file(filename="", text=""):
    """jr"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
