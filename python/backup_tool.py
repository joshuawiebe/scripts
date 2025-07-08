#!/usr/bin/env python3
"""
File: python/backup_tool.py
Usage: python backup_tool.py /path/to/source /path/to/destination/dir
"""

import sys
import os
import tarfile
from datetime import datetime

def create_backup(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        print(f"Source directory not found: {src_dir}")
        sys.exit(1)
    os.makedirs(dest_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = os.path.join(dest_dir, f"backup_{timestamp}.tar.gz")
    
    print(f"Creating backup {archive_name} …")
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(src_dir, arcname=os.path.basename(src_dir))
    print("Backup complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    _, source, destination = sys.argv
    create_backup(source, destination)
