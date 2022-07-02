import time


class Trainer:
    def __init__(self):
      self.metric_start = None
      self.first_start = None
      self.current_metric_name = None
      self.metrics = {}

    def __enter__(self):
        if not self.current_metric_name:
            raise ValueError('Metric name was not specified')

        self.metric_start = time.time()

        if not self.first_start:
            self.first_start = self.metric_start

    def __exit__(self, exc_type, exc_value, traceback):
        self._append_metric(self.current_metric_name, self.metric_start, time.time())

    def __call__(self, name: str) -> 'Trainer':
        self.current_metric_name = str(name)
        return self

    def start_measuring(self) -> 'Trainer' :
       self.first_start = time.time()
       return self

    def add_total(self, name='total_execution'):
        if not self.first_start:
            raise ValueError('Measuring was not started.'
                'Add at least one metric or call start_measuring()')
        self._append_metric(str(name), self.first_start, time.time())

    def _append_metric(self, name: str, start: float, end: float):
        self.metrics[name] = {
            'start': start,
            'end': end,
            'interval': end - start,
        }
