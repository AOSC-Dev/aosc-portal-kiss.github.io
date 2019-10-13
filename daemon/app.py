import falcon
import requests
import watcher
import sys
import logging
import threading
import json


class MirrorQueryResource(object):
    def on_get(self, req, resp):
        resp.body = json.dumps(data['m'])


data = {'m': {}}


def run_watcher():
    watcher_process = watcher.Watcher('mirrors.yml', data)
    watcher_thread = threading.Thread(target=watcher_process.start)
    watcher_thread.daemon = True
    watcher_thread.start()


application = falcon.API()
application.add_route('/api/mirrors', MirrorQueryResource())
logging.basicConfig(level=logging.INFO)
run_watcher()
