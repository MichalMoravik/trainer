import unittest

from trainer import Trainer, DummyTrainer


class IntegrationTests(unittest.TestCase):
    def test_switching_to_dummy(self):
        CONFIG_VAR = False

        trainer = Trainer() if CONFIG_VAR else DummyTrainer()

        m = trainer.round(4).start_measuring().add_total().metrics

        self.assertDictEqual(m, {})


if __name__ == '__main__':
    unittest.main()

