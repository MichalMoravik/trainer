import unittest

from trainer import Trainer


class TrainerTest(unittest.TestCase):
    def test_adding_to_metrics(self):
        trainer = Trainer()
        with trainer('r'):
            pass

        self.assertIsNotNone(trainer.metrics['r'])


if __name__ == '__main__':
    unittest.main()
