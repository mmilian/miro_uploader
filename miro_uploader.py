#!/usr/bin/env python3

import sys
import time
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from shutil import copy2
from os import remove


def main():
    if len(sys.argv) < 2:
        print(f"Error: At least one arg is required. Usage: miro_uploader <destination_path> [monitored_path]")
        exit(1)

    destination_path = sys.argv[1]
    monitored_path = sys.argv[2] if len(sys.argv) > 2 else '.'

    def on_created(event):
        print(f"hey, {event.src_path} has been created!")

    def on_modified(event):
        try:
            print(f"hey buddy, {event.src_path} has been modified")
            return_path = copy2(event.src_path, destination_path)
            print(f"hey, that a copy path {return_path}")
            remove(event.src_path)
        except Exception:
            pass

    event_handler = RegexMatchingEventHandler(regexes=[r"^[\x00-\x7F]*jpg$"],
                                              ignore_directories=True, case_sensitive=False)
    event_handler.on_created = on_created
    event_handler.on_modified = on_modified
    observer = Observer()
    observer.schedule(event_handler, monitored_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
