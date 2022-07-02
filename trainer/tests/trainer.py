import unittest
import time

from trainer import Trainer


class TrainerTest(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainer()

    def test_append_metric(self):
        start = 1656752928.3975601
        end = 1656752955.581867
        expected = {'r': {
            'start': start,
            'end': end,
            'interval': end - start
        }}

        self.trainer._append_metric('r', start, end)

        self.assertEqual(self.trainer.metrics, expected)

    def test_add_total_when_metric(self):
        with self.trainer('n'):
            pass

        self.trainer.add_total()

        self.assertIsNotNone(self.trainer.metrics.get('total_execution'))

    def test_add_total_when_started(self):
        self.trainer.start_measuring()

        self.trainer.add_total()

        self.assertIsNotNone(self.trainer.metrics.get('total_execution'))


if __name__ == '__main__':
    unittest.main()
