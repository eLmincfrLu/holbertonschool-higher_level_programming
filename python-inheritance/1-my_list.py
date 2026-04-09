#!/usr/bin/python3
"""
Bu modul MyList klasını təqdim edir.
"""


class MyList(list):
    """Siyahıdan miras alan klas."""

    def print_sorted(self):
        """Siyahını sıralanmış şəkildə çap edir."""
        print(sorted(self))