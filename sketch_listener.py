import time
import sys
import os
import pdb


try:
    import watchdog
    print("Watchdog is installed")
    from watchdog.observers import Observer
    from watchdog.events import PatternMatchingEventHandler

    import pdb
    print("Application attached to terminal")

except ImportError:
    print("watchdog not installed. Will attempt installation")
    import pip
    pip.main(['install', 'watchdog'])
    print("watchdog now installed")
    from watchdog.observers import Observer
    from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.png", "*.jpeg", "*.jpg"]

    def __init__(self, switch):
        PatternMatchingEventHandler.__init__(self)
        self.switch = int(switch)

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        filename = os.path.basename(event.src_path)
        print(event.src_path, event.event_type)  # print now only for debugging
        print("pushing file to Android through adb: " + filename)
        print("converting to jpg")

        os.system("adb push " + filename + " /sdcard/Download/file.jpg")
        os.system("adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Download/file.jpg -t image/jpeg")


    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def set_switch(switch):
        self.switch = 0



if __name__ == '__main__':
    args = sys.argv[1:] # command line arguments passed to a Python script. The first argument is the folder path to watch.
    observer = Observer()
    user_input = input("Please choose 0 for Display or 1 for Phone: ")
    print("You chose " + user_input)
    print("starting Observer")
    handler = MyHandler(user_input)
    observer.schedule(handler, path=args[0] if args else '.') # take whatever folder path is given to me
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()





 