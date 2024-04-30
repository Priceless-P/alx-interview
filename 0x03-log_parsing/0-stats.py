#!/usr/bin/python3
"""Log parsing"""
import sys
from collections import defaultdict


def parse_log():
    """Reads stdin line by line and computes metrics"""
    total_file_size = 0
    line_count = 0
    status_code_count = defaultdict(int)

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()

            if len(parts) != 9:
                continue
            status_code = parts[7]
            file_size = int(parts[8])

            total_file_size += file_size
            status_code_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_count)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_count)


def print_stats(total_file_size, status_code_count):
    """Prints stats"""
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_count):
        print("{}: {}".format(status_code, status_code_count[status_code]))


if __name__ == "__main__":
    parse_log()
