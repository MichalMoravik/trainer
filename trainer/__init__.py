import time


class Trainer:
    def __init__(self):
      self.start = 0
      self.first_start = 0
      self.current_measurement_name = None
      self.metrics = {}

    def __enter__(self):
        self.start = time.time()

        if self.first_start == 0:
            self.first_start = self.start

    def __exit__(self, exc_type, exc_value, traceback):
        self.metrics[self.current_measurement_name] = {
            'start': self.start,
            'end': time.time(),
            'interval': time.time() - self.start
        }

    def __call__(self, name):
        self.current_measurement_name = name
        return self

    def add_total(self, name='total_execution'):
        end = time.time()

        self.metrics[name] = {
                'start': self.first_start,
                'end': end,
                'interval': end - self.first_start
        }
