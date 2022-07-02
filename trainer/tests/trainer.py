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

    def test_ctx_appends(self):
        with self.trainer('t'):
            pass
        self.assertIsNotNone(self.trainer.metrics.get('t'))

    def test_ctx_without_name_fail(self):
        with self.assertRaises(Exception):
            with self.trainer:
                pass

    def test_add_total_when_metric(self):
        with self.trainer('n'):
            pass

        self.assertIsNotNone(
            self.trainer.add_total().metrics.get('total_execution')
        )

    def test_add_total_when_started(self):
        self.trainer.start_measuring()

        self.assertIsNotNone(
            self.trainer.add_total().metrics.get('total_execution')
        )

    def test_add_total_fail(self):
        with self.assertRaises(Exception):
            self.trainer.add_total()


if __name__ == '__main__':
    unittest.main()
