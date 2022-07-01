import time


class Trainer:
    def __init__(self):
      self.last_start = 0
      self.last_end = 0
      self.first_start = 0
      self.current_measurement_name = None
      self.metrics = {}

    def __enter__(self):
        self.last_start = time.time()

        if self.first_start == 0:
            self.first_start = self.last_start

    def __exit__(self, exc_type, exc_value, traceback):
        self.last_end = time.time()

        self.metrics[self.current_measurement_name] = {
            'start': self.last_start,
            'end': self.last_end,
            'interval': self.last_end - self.last_start
        }

    def __call__(self, name):
        self.current_measurement_name = name
        return self

    def add_total(self, name='total_execution'):
        self.last_end = time.time()

        self.metrics[name] = {
                'start': self.first_start,
                'end': self.last_end,
                'interval': self.last_end - self.first_start
        }
