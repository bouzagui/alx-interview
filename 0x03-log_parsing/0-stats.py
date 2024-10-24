#!/usr/bin/python3
"""Doc"""
import sys
import signal

total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler():
    """Handles keyboard interruption"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue

        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        continue
