from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(" "):
            src = folder_to_track + "/" + filename
            new_destination = folder_desination + "/" + filename
            os.rename(src, new_destination)
folder_to_track = "/Users/Rendrag/Desktop/myFolder"
folder_destination = "/Users/Rendrag/Desktop/newFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        print('Running')
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    print('Moved')
observer.join()
