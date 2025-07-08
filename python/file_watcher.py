#!/usr/bin/env python3
"""
File: tools/file_watcher.py
Usage: python file_watcher.py /path/to/watch log.txt
"""

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        with open(log_file, "a") as log:
            log.write(f"{time.ctime()}: {event.event_type} {event.src_path}\n")
        print(f"Logged: {event.event_type} {event.src_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    watch_dir, log_file = sys.argv[1], sys.argv[2]

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=watch_dir, recursive=True)
    observer.start()
    print(f"Watching {watch_dir}. Logging to {log_file}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Stopped watching.")
