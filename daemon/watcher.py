import requests
import time
import yaml
import logging
import threading
import signal


def parse_config(filename: str) -> dict:
    with open(filename, 'rt') as f:
        return yaml.safe_load(f)


def get_last_modified(url: str) -> int:
    last_updated_url = '%s/last_update' % url.rstrip('/')
    try:
        response = requests.get(last_updated_url, timeout=10)
        response.raise_for_status()
    except Exception:
        logging.error('Unable to fetch the status from %s' % url)
        return -1
    try:
        return int(response.text.strip())
    except Exception:
        logging.error('Unable to parse the status from %s' % url)
        return -1


class Watcher(object):
    def __init__(self, config: str, data: dict):
        self.config_file = config
        self.config = {}
        self.results = data
        self.reload(config)

    def start(self) -> None:
        logging.info("Starting Watcher...")
        while True:
            results = {'ref': 0, 'mirrors': []}
            reference = get_last_modified(self.config['repo']['url'])
            if reference < 0:
                time.sleep(300)
                continue
            for mirror in self.config['mirrors']:
                current = {
                    'name': mirror['name'],
                    'region': mirror['region'],
                    'url': mirror['url'],
                    'updated': get_last_modified(mirror['url']),
                    'checked': time.time()
                }
                results['mirrors'].append(current)
            results['ref'] = reference
            self.results['m'] = results
            time.sleep(300)


    def reload_on_signal(self) -> None:
        return self.reload(self.config_file)

    def reload(self, config: str) -> None:
        logging.info('loading config file: {}'.format(config))
        try:
            self.config = parse_config(config)
            logging.info('config loaded.')
        except Exception as e:
            logging.exception(e)
