class DummyTrainer:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __call__(self, name: str) -> 'DummyTrainer':
        return self

    def start_measuring(self) -> 'DummyTrainer':
       return self

    def round(self, no=None) -> 'DummyTrainer':
        return self

    def add_total(self, name='total_execution') -> 'DummyTrainer':
        return self

    def _append_metric(self, name: str, start: float, end: float):
        pass

