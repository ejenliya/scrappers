from pathlib import Path
from time import sleep

from watchdog.observers import Observer

from EventHandler import EventHandler

if __name__ == '__main__':
    watch_path = Path(r'C:\Users\georg\Downloads')
    destination_root = Path(r'D:\поиски\website')
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root, name='test')

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()