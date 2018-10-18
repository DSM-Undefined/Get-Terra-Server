import os
import threading
import time

from flask import request

from app import create_app

app = create_app()


def reload_server():
    time.sleep(2)

    os.system('. ../hook.sh')


@app.route('/hook', methods=['POST'])
def webhook_event_handler():
    if request.headers['X-GitHub-Event'] == 'push':
        threading.Thread(target=reload_server).start()

    return 'hello'


if __name__ == '__main__':
    app.run('0.0.0.0', port=1234)
