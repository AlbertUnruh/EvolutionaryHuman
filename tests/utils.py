import unittest
import random
from EvolutionaryHuman import utils


class TestUtils(unittest.TestCase):
    def test0_random(self):
        utils.set_random_seed("TestCase")
        self.assertNotEqual(
            random.random(),
            random.random(),
        )

        # make sure the seed is working
        utils.set_random_seed("TestCase")
        first = random.random()
        utils.set_random_seed("TestCase")
        second = random.random()
        self.assertEqual(
            first,
            second,
        )

    def test1_age_occurrence(self):
        self.assertEqual(
            utils.age_occurrence(42),
            utils.age_occurrence(42),
        )

    def test2_random_age(self):
        utils.set_random_seed("TestCase")
        results = {}
        for i in range(120 + 1):
            results[i] = 0
        for i in range(1000):
            results[utils.get_random_age()] += 1
        self.assertEqual(
            results,
            # fmt: off
            {
                # results with the seed "TestCase"
                0: 20, 1: 18, 2: 16, 3: 13, 4: 23, 5: 24, 6: 19, 7: 15, 8: 11, 9: 18,
                10: 17, 11: 16, 12: 19, 13: 17, 14: 13, 15: 18, 16: 18, 17: 12, 18: 21, 19: 13,
                20: 21, 21: 21, 22: 15, 23: 15, 24: 11, 25: 9, 26: 19, 27: 14, 28: 18, 29: 5,
                30: 14, 31: 19, 32: 12, 33: 14, 34: 16, 35: 13, 36: 15, 37: 16, 38: 16, 39: 10,
                40: 15, 41: 11, 42: 14, 43: 13, 44: 12, 45: 12, 46: 8, 47: 18, 48: 12, 49: 17,
                50: 15, 51: 12, 52: 7, 53: 12, 54: 10, 55: 14, 56: 10, 57: 7, 58: 8, 59: 6,
                60: 11, 61: 9, 62: 2, 63: 12, 64: 6, 65: 3, 66: 6, 67: 5, 68: 5, 69: 7,
                70: 5, 71: 3, 72: 6, 73: 2, 74: 1, 75: 2, 76: 1, 77: 2, 78: 2, 79: 2,
                80: 6, 81: 3, 82: 2, 83: 1, 84: 3, 85: 2, 86: 1, 87: 1, 88: 0, 89: 3,
                90: 2, 91: 1, 92: 0, 93: 0, 94: 1, 95: 2, 96: 1, 97: 1, 98: 1, 99: 0,
                100: 1, 101: 2, 102: 1, 103: 3, 104: 1, 105: 0, 106: 0, 107: 0, 108: 0, 109: 0,
                111: 0, 110: 0, 112: 0, 113: 0, 114: 0, 115: 0, 116: 1, 117: 0, 118: 0, 119: 1,
                120: 0
            },
            # fmt: on
        )

    def test3_random_name(self):
        utils.set_random_seed("TestCase")
        self.assertNotEqual(
            utils.get_random_name(),
            utils.get_random_name(),
        )

        utils.set_random_seed("TestCase")
        self.assertEqual(
            utils.get_random_name(),
            "Anthony",
        )

        utils.set_random_seed("TestCase")
        self.assertEqual(
            utils.get_random_name(gender="male"),
            "Robinson",
        )

        utils.set_random_seed("TestCase")
        self.assertEqual(
            utils.get_random_name(gender="female"),
            "Quianna",
        )


if __name__ == "__main__":
    unittest.main()
