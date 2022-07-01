import unittest


class TrainerTest(unittest.TestCase):
    def test_if_says_hi(self):
        actual = 'hi'
        self.assertEqual(actual, 'hi')


if __name__ == '__main__':
    unittest.main()
