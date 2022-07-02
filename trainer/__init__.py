import time


class Trainer:
    def __init__(self):
      self.start = 0
      self.first_start = None
      self.current_measurement_name = None
      self.metrics = {}

    def __enter__(self):
        self.start = time.time()

        if self.first_start == 0:
            self.first_start = self.start

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.current_measurement_name:
            raise ValueError('Name of the current measurement was not specified')
        self._append_metric(self.current_measurement_name, self.start, time.time())

    def __call__(self, name: str) -> 'Trainer':
        self.current_measurement_name = name
        return self

    def add_total(self, name='total_execution') -> 'Trainer':
        if not self.first_start:
            raise ValueError('')
        self._append_metric(name, self.first_start, time.time())
        return self

    def _append_metric(self, name: str, start: float, end: float):
        self.metrics[name] = {
            'start': start,
            'end': end,
            'interval': end - start,
        }
