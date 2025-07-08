#!/usr/bin/env python3
"""
File: tools/url_status_checker.py
Usage: python url_status_checker.py urls.txt report.csv
"""

import sys
import csv
import requests

def check_urls(source_file, output_file):
    with open(source_file) as f:
        urls = [line.strip() for line in f if line.strip()]
    results = []
    for url in urls:
        try:
            r = requests.head(url, timeout=5)
            code = r.status_code
        except Exception as e:
            code = f"ERROR: {e}"
        results.append((url, code))
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URL", "Status"])
        writer.writerows(results)
    print(f"Checked {len(urls)} URLs. Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    check_urls(sys.argv[1], sys.argv[2])
