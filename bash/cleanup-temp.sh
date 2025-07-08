#!/usr/bin/env bash
# File: bash/cleanup-temp.sh
# Usage: ./cleanup-temp.sh [DIR] [DAYS]
# Default: DIR=/tmp, DAYS=7

TARGET_DIR="${1:-/tmp}"
RETENTION_DAYS="${2:-7}"

echo "Cleaning files in $TARGET_DIR older than $RETENTION_DAYS days..."
find "$TARGET_DIR" -type f -mtime +"$RETENTION_DAYS" -print -delete
echo "Done."
