import unittest
import time
import math

from parameterized import parameterized

from trainer import Trainer


class TrainerTest(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainer()

    def test_ctx_appends(self):
        with self.trainer('t'):
            pass

        self.assertIsNotNone(self.trainer.metrics.get('t'))

    def test_ctx_appends_twice(self):
        with self.trainer('t'):
            pass
        with self.trainer('m'):
            pass

        self.assertIsNotNone(self.trainer.metrics.get('m'))
        self.assertIsNotNone(self.trainer.metrics.get('t'))

    def test_ctx_should_fail_to_append_duplicated_name(self):
        with self.trainer('t'):
            pass

        with self.assertRaises(Exception):
            with self.trainer('t'):
                pass

    def test_ctx_without_name_fail(self):
        with self.assertRaises(Exception):
            with self.trainer:
                pass

        with self.assertRaises(Exception):
            with self.trainer(''):
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

    @parameterized.expand([
        (1, ),
        (2, ),
    ])
    def test_round(self, no):
        self.trainer.round(no).start_measuring()
        time.sleep(math.pi / 10)
        m = self.trainer.add_total().metrics

        for v in m['total_execution'].values():
            decimals_number = len(str(v)[str(v).find('.')+1:])
            self.assertLessEqual(decimals_number, no)

    @parameterized.expand([
        (-2, ),
        (-1, ),
    ])
    def test_round_fail(self, no):
        with self.assertRaises(Exception):
            self.trainer.round(no)

    def test_round_empty(self):
        self.trainer.round().start_measuring()
        time.sleep(math.pi / 10)
        m = self.trainer.add_total().metrics

        for v in m['total_execution'].values():
            self.assertTrue(type(v) is int)

    def test_round_zero(self):
        self.trainer.round(0).start_measuring()
        time.sleep(math.pi / 10)
        m = self.trainer.add_total().metrics

        for v in m['total_execution'].values():
            self.assertTrue(type(v) is int)

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


if __name__ == '__main__':
    unittest.main()
