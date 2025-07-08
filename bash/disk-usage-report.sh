#!/usr/bin/env bash
# File: bash/disk-usage-report.sh
# Usage: ./disk-usage-report.sh [EMAIL] [DIR...]
# Sends an email to EMAIL with du -sh results for each DIR. Defaults: EMAIL=user@localhost, DIR=/home

EMAIL="${1:-user@localhost}"
shift || true
DIRS=("${@:-/home}")

TMPFILE=$(mktemp)

echo "Disk Usage Report - $(date)" >"$TMPFILE"
for d in "${DIRS[@]}"; do
  if [ -d "$d" ]; then
    du -sh "$d" >>"$TMPFILE"
  else
    echo "Directory not found: $d" >>"$TMPFILE"
  fi
done

mail -s "Disk Usage Report" "$EMAIL" <"$TMPFILE"
rm -f "$TMPFILE"
echo "Report sent to $EMAIL."
