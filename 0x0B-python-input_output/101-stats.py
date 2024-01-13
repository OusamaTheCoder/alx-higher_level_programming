#!/usr/bin/python3
"""
Prints summary statistics for a given log file.
"""


import sys


def print_stats(total_size, status_codes):
    """
    Prints summary statistics for a given log file.
    """
    print("File size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{:d}: {:d}".format(code, count))
