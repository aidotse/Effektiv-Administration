import time
from watchdog.events import FileSystemEventHandler
from watchdog import events
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
from watchdog import events

from watcher_utils.update_db import load_file, remove_file, update_file

class WatcherHandler(FileSystemEventHandler):

    def on_modified(self, event: events.FileModifiedEvent):
        try:
            if event.is_directory:
                return
            update_file(event.src_path)
            print("\n" * 50)
            print(f'Modified file: {event.src_path}')
        except:
            pass

    def on_created(self, event:events.FileCreatedEvent):
        try:
            if event.is_directory:
                return
            load_file(event.src_path)
            print("\n" * 50)
            print(f'Created file: {event.src_path}')
        except:
            pass

    def on_deleted(self, event:events.FileDeletedEvent):
        try:
            if event.is_directory:
                return
            remove_file(event.src_path)
            print("\n" * 50)
            print(f'Deleted file: {event.src_path}')
        except:
            pass

        

def start_watcher(directory):
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