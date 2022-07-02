import unittest

from trainer import Trainer


class TrainerTest(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainer()

    def test_adding_to_metrics(self):
        with self.trainer('r'):
            pass

        self.assertIsNotNone(self.trainer.metrics.get('r'))

    def test_add_total(self):
        self.trainer.add_total()

        self.assertIsNotNone(self.trainer.metrics.get('total_execution'))


if __name__ == '__main__':
    unittest.main()
