import time

from watchdog import events
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver

from utils.watcher.update_db import load_file, remove_file, update_file


class WatcherHandler(FileSystemEventHandler):
    def on_modified(self, event: events.FileModifiedEvent):
        if event.is_directory:
            return
        update_file(event.src_path)
        print("\n" * 50)
        print(f"Modified file: {event.src_path}")

    def on_created(self, event: events.FileCreatedEvent):
        if event.is_directory:
            return
        load_file(event.src_path)
        print("\n" * 50)
        print(f"Created file: {event.src_path}")

    def on_deleted(self, event: events.FileDeletedEvent):
        if event.is_directory:
            return
        remove_file(event.src_path)
        print("\n" * 50)
        print(f"Deleted file: {event.src_path}")


def start_watcher(directory):
    """
    Starts the watcher on a specified directory that notifies and handles creation/changes/deletion of files within
    that directory so that the ChromaDB reflects the information contained in the directory"""
    event_handler = WatcherHandler()
    observer = PollingObserver()
    observer.schedule(event_handler, directory, recursive=True)

    observer.start()
    print(f"Started watcher on {directory}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
