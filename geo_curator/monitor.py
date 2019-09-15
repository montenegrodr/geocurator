from prometheus_client import start_http_server, Counter


class Monitor(object):
    """
    Export application metrics through prometheus
    """
    def __init__(self, port):
        """
        Parameters
        ----------
        port : int
            prometheus port
        """
        self._port = port
        self._fatal_errors_total = Counter(
            'geo_curator_fatal_errors',
            'Number of fatal errors from curator job'
        )

    def start(self):
        """
        Start prometheus exporter server
        """
        start_http_server(self._port)

    def fatal_errors(self):
        """
        Increment fatal error counter
        """
        self._fatal_errors_total.inc()
