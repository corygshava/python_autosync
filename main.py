from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import json
from datetime import datetime

# my local codes
from uploader import send2server

# this code handles watching for changes in the folder

class Watcher:
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.folder_to_watch, recursive=False)
        self.observer.start()
        print(f"\nWatching folder: {self.folder_to_watch}\n")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def log_event(self, action, path):
        filename = os.path.basename(path)
        log_entry = {
            "operation": action,
            "filename": filename,
            "time": datetime.now().isoformat()
        }
        print(f"{action}: {filename}")
        history = []
        if os.path.exists("history.json"):
            with open("history.json", "r") as log_file:
                try:
                    history = json.load(log_file)
                except json.JSONDecodeError:
                    history = []
        history.append(log_entry)
        with open("history.json", "w") as log_file:
            json.dump(history, log_file, indent=4)

    def on_created(self, event):
        if not event.is_directory:
            self.log_event("Added", event.src_path)
            tryuploading(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event("Modified", event.src_path)
            tryuploading(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_event("Deleted", event.src_path)
            trydeleting(event.src_path)

def tryuploading(who):
    send2server(f"{who}",f"{folder_path}","update",upload_url);

def trydeleting(who):
    send2server(f"{who}",f"{folder_path}","delete",upload_url);

# the folder you want to monitor
entered = input("which folder will we be monitoring: ");
folder_path = "watchme";

# where the data will be uploaded
entered = input("paste the link of the uploader API endpoint: ");
upload_url = entered or "http://localhost/pyplay/py_api_uploader.php";

watcher = Watcher(folder_path)
watcher.run()
