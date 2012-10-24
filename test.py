import unittest
from myna import *

class TestMyna(unittest.TestCase):
    def setUp(self):
        self.expt = Experiment('45923780-80ed-47c6-aa46-15e2ae7a0e8c')

    def test_suggest(self):
        suggestion = self.expt.suggest()
        self.assertIsInstance(suggestion, Suggestion)

    def test_suggest_bogus_uuid(self):
        with self.assertRaises(MynaError):
            Experiment('i-dont-exist').suggest()

    def test_reward(self):
        suggestion = self.expt.suggest()
        ok = suggestion.reward()
        self.assertTrue(ok)

    def test_reward_bad_amount(self):
        suggestion = self.expt.suggest()
        with self.assertRaises(MynaError):
            suggestion.reward(2.0)
