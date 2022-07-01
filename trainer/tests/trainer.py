import unittest

from trainer import Trainer


class TrainerTest(unittest.TestCase):
    def test_adding_to_metrics(self):
        trainer = Trainer()

        with trainer('r'):
            pass

        self.assertIsNotNone(trainer.metrics.get('r'))

    def test_add_total(self):
        trainer = Trainer()

        trainer.add_total()

        self.assertIsNotNone(trainer.metrics.get('total_execution'))


if __name__ == '__main__':
    unittest.main()
