import time


class Trainer():
    first_start = None

    def __enter__(self):
        self.first_start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        pass
