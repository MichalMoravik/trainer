import time


class Trainer:
    def __init__(self):
      self._metric_start = None
      self._first_start = None
      self._current_metric_name = None
      self._dec_no = None
      self.metrics = {}

    def __enter__(self):
        if not self._current_metric_name:
            raise ValueError('Metric name was not specified')

        self._metric_start = time.time()

        if not self._first_start:
            self._first_start = self._metric_start

    def __exit__(self, exc_type, exc_value, traceback):
        self._append_metric(
            self._current_metric_name, self._metric_start, time.time()
        )

    def __call__(self, name: str) -> 'Trainer':
        self._current_metric_name = str(name)
        return self

    def start_measuring(self) -> 'Trainer':
       self._first_start = time.time()
       return self

    def round(self, no) -> 'Trainer':
        self._dec_no = no
        return self

    def add_total(self, name='total_execution') -> 'Trainer':
        if not self._first_start:
            raise ValueError('Measuring was not started.'
                'Add at least one metric or call start_measuring()')
        self._append_metric(str(name), self._first_start, time.time())
        return self

    def _append_metric(self, name: str, start: float, end: float):
        r = lambda n: round(n, self._dec_no) if self._dec_no else n

        self.metrics[name] = {
            'start': r(start),
            'end': r(end),
            'interval': r(end) - r(start),
        }
