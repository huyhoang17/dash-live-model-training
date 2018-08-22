import logging
import time
from app import app
import multiprocessing

def run():
    app.server.logger.disabled = True
    log = logging.getLogger('werkzeug')
    # log.disabled = True
    log.setLevel(logging.ERROR)
    app.run_server(port=8051, debug=False, processes=1, threaded=False)


if __name__ == '__main__':
    print("Starting")

    process = multiprocessing.Process(target=run)
    process.start()

    time.sleep(5)
    print("Stopped sleeping")

    for x in range(1000):
        print(x)
        time.sleep(0.2)
