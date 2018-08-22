import os
import sys
import logging
import time
import multiprocessing

from app import app


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class Viewer(object):
    def __init__(self,
                 supress_flask=True,
                 port=8055,
                 wait_time=5):
        self.port = port
        self.supress_flask = supress_flask
        self.wait_time = wait_time

    def run(self):
        log = logging.getLogger('werkzeug')

        if self.supress_flask:
            log.setLevel(logging.ERROR)

        app.run_server(port=self.port, debug=False, processes=1,
                       threaded=False)

    def open(self):
        process = multiprocessing.Process(target=self.run)
        process.start()
        time.sleep(self.wait_time)


if __name__ == '__main__':
    print("Starting")

    Viewer().open()

    time.sleep(5)
    print("Stopped sleeping")

    for x in range(1000):
        print(x)
        time.sleep(0.2)
