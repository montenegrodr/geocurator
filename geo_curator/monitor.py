from prometheus_client import start_http_server, Counter


class Monitor(object):
    def __init__(self, port):
        self._port = port
        self._fatal_errors_total = Counter(
            'geo_curator_fatal_errors',
            'Number of fatal errors from curator job'
        )

    def start(self):
        start_http_server(self._port)

    def fatal_errors(self):
        self._fatal_errors_total.inc()
