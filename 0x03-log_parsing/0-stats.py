#!/usr/bin/python3
"""Log parsing script to count HTTP status codes and total file sizes."""

import sys

# Initialize status counts
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_metrics(status_counts, total_size):
    """Prints the metrics of the log parsing."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def main():
    """Main function to parse the log input."""
    count = 0
    total_size = 0

    try:
        for code in sys.stdin:
            if count != 0 and count % 10 == 0:
                print_metrics(status_counts, total_size)

            parts = code.split()
            count += 1

            # Add to total size, if possible
            try:
                total_size += int(parts[-1])
            except (ValueError, IndexError):
                print(f"Warning: Unable to parse size from line: {code.strip()}")
                continue

            # Count status codes
            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                print(f"Warning: Unable to parse status code from line: {code.strip()}")

        print_metrics(status_counts, total_size)

    except KeyboardInterrupt:
        print_metrics(status_counts, total_size)
        raise

if __name__ == "__main__":
    main()
