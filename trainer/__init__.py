import time


class Trainer:
    def __init__(self):
      self.start = None
      self.first_start = None
      self.current_metric_name = None
      self.metrics = {}

    def __enter__(self):
        self.start = time.time()

        if not self.first_start:
            self.first_start = self.start

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.current_metric_name:
            raise ValueError('Name of the current measurement was not specified')
        self._append_metric(self.current_metric_name, self.start, time.time())

    def __call__(self, name: str) -> 'Trainer':
        self.current_metric_name = name
        return self

    def start_measuring(self):
       self.first_start = time.time()

    def add_total(self, name='total_execution'):
        if not self.first_start:
            raise ValueError('Measuring was not started.'
                'Add at least one metric or call start_measuring()')
        self._append_metric(name, self.first_start, time.time())

    def _append_metric(self, name: str, start: float, end: float):
        self.metrics[name] = {
            'start': start,
            'end': end,
            'interval': end - start,
        }
