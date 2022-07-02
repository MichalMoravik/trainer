import time


class Trainer:
    def __init__(self):
      self._metric_start = None
      self._first_start = None
      self._current_metric_name = None
      self._round = lambda i: i
      self.metrics = {}

    def __enter__(self):
        if not self._current_metric_name:
            raise ValueError('Metric name was not specified')

        self._metric_start = time.time()

        if not self._first_start:
            self._first_start = self._metric_start

    def __exit__(self, exc_type, exc_value, traceback):
        self._append_metric(
            str(self._current_metric_name), self._metric_start, time.time()
        )

    def __call__(self, name: str) -> 'Trainer':
        if str(name) in self.metrics:
            raise ValueError('Metric with this name already exists')
        self._current_metric_name = name
        return self

    def start_measuring(self) -> 'Trainer':
       self._first_start = time.time()
       return self

    def round(self, no=None) -> 'Trainer':
        if no == 0 or no is None:
            self._round = lambda n: round(n)
            return self
        if int(no) < 0:
            raise ValueError('Round argument must be unsigned integer or absent')
        self._round = lambda n: round(n, int(no))
        return self

    def add_total(self, name='total_execution') -> 'Trainer':
        if not self._first_start:
            raise ValueError(
                'Cannot add total as measurement has not been started. '
                'Add at least one metric or call start_measuring()'
            )
        self._append_metric(str(name), self._first_start, time.time())
        return self

    def _append_metric(self, name: str, start: float, end: float):
        self.metrics[name] = {
            'start': self._round(start),
            'end': self._round(end),
            'interval': self._round(self._round(end) - self._round(start)),
        }

