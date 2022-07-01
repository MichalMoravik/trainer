import time


class Trainer:
    def __init__(self):
      self.start = 0
      self.current_measurement_name = None
      self.metrics = {}

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.metrics[self.current_measurement_name] = {
            'start': self.start,
            'end': time.time(),
            'interval': time.time() - self.start
        }

    def __call__(self, name):
        self.current_measurement_name = name
        return self
