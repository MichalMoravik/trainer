import unittest

from trainer import Trainer


class TrainerTest(unittest.TestCase):
    def test_first_start(self):
       trainer = Trainer()

       with trainer:
           pass

       print(trainer.first_start)
       self.assertIsNotNone(trainer.first_start)


if __name__ == '__main__':
    unittest.main()
