import os
import sys
import logging
import time
import multiprocessing

from app import app


class Viewer(object):
    def __init__(self,
                 suppress_flask=True,
                 port=8055,
                 wait_time=10):
        self.port = port
        self.suppress_flask = suppress_flask
        self.wait_time = wait_time
        self.process = multiprocessing.Process(target=self._run)

    def _run(self):
        log = logging.getLogger('werkzeug')
        if self.suppress_flask:
            log.setLevel(logging.ERROR)

        app.run_server(port=self.port,
                       debug=False,
                       processes=1,
                       threaded=True)

    def open(self):
        if not self.process.is_alive():
            self.process.start()
            time.sleep(self.wait_time)
            print("Open your viewer at 127.0.0.1:" + str(self.port))

    def close(self, force=False):
        if self.process.is_alive():
            if force:
                self.process.kill()
            else:
                self.process.terminate()


if __name__ == '__main__':
    print("Starting Viewer")
    viewer = Viewer()
    viewer.open()

    print("Starting For Loop")
    for x in range(1000):
        print(x)
        time.sleep(0.2)

    viewer.close()
    print("Viewer closed")
