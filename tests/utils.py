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
                0: 20, 1: 18, 2: 16, 3: 13, 4: 23, 5: 24, 6: 19, 7: 15, 8: 11, 9: 18, 10: 17, 11: 16, 12: 19, 13: 17,
                14: 13, 15: 18, 16: 18, 17: 12, 18: 21, 19: 13, 20: 21, 21: 21, 22: 15, 23: 15, 24: 11, 25: 9, 26: 19,
                27: 14, 28: 18, 29: 5, 30: 14, 31: 19, 32: 12, 33: 14, 34: 16, 35: 13, 36: 15, 37: 16, 38: 16, 39: 10,
                40: 15, 41: 11, 42: 14, 43: 13, 44: 12, 45: 12, 46: 8, 47: 18, 48: 12, 49: 17, 50: 15, 51: 12, 52: 7,
                53: 12, 54: 10, 55: 14, 56: 10, 57: 7, 58: 8, 59: 6, 60: 11, 61: 9, 62: 2, 63: 12, 64: 6, 65: 3, 66: 6,
                67: 5, 68: 5, 69: 7, 70: 5, 71: 3, 72: 6, 73: 2, 74: 1, 75: 2, 76: 1, 77: 2, 78: 2, 79: 2, 80: 6, 81: 3,
                82: 2, 83: 1, 84: 3, 85: 2, 86: 1, 87: 1, 88: 0, 89: 3, 90: 2, 91: 1, 92: 0, 93: 0, 94: 1, 95: 2, 96: 1,
                97: 1, 98: 1, 99: 0, 100: 1, 101: 2, 102: 1, 103: 3, 104: 1, 105: 0, 106: 0, 107: 0, 108: 0, 109: 0,
                111: 0, 110: 0, 112: 0, 113: 0, 114: 0, 115: 0, 116: 1, 117: 0, 118: 0, 119: 1, 120: 0
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

    def test4_random_iq(self):
        utils.set_random_seed("TestCase")
        results = {}
        for i in range(40, 160 + 1):
            results[i] = 0
        for i in range(1000):
            results[utils.get_random_iq()] += 1
        self.assertEqual(
            results,
            # fmt: off
            {
                # results with the seed "TestCase"
                40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 48: 0, 49: 0, 50: 0, 51: 0, 52: 0, 53: 0, 54: 0,
                55: 0, 56: 0, 57: 0, 58: 0, 59: 1, 60: 1, 61: 1, 62: 2, 63: 1, 64: 1, 65: 2, 66: 4, 67: 2, 68: 5, 69: 4,
                70: 5, 71: 4, 72: 5, 73: 3, 74: 9, 75: 4, 76: 6, 77: 7, 78: 13, 79: 15, 80: 14, 81: 15, 82: 11, 83: 14,
                84: 10, 85: 19, 86: 18, 87: 19, 88: 21, 89: 18, 90: 21, 91: 22, 92: 21, 93: 26, 94: 33, 95: 23, 96: 22,
                97: 19, 98: 27, 99: 20, 100: 25, 101: 24, 102: 27, 103: 25, 104: 28, 105: 23, 106: 20, 107: 26, 108: 19,
                109: 22, 110: 24, 111: 30, 112: 18, 113: 18, 114: 20, 115: 15, 116: 14, 117: 14, 118: 10, 119: 15,
                120: 6, 121: 13, 122: 9, 123: 8, 124: 8, 125: 3, 126: 2, 127: 3, 128: 8, 129: 5, 130: 3, 131: 4, 132: 1,
                133: 4, 134: 2, 135: 0, 136: 4, 137: 1, 138: 1, 139: 3, 140: 4, 141: 1, 142: 0, 143: 0, 144: 0, 145: 0,
                146: 0, 147: 0, 148: 0, 149: 1, 150: 0, 151: 0, 152: 0, 153: 1, 154: 0, 155: 0, 156: 0, 157: 0, 158: 0,
                159: 0, 160: 0
            },
            # fmt: on
        )


if __name__ == "__main__":
    unittest.main()
