import typing
import unittest
from EvolutionaryHuman import utils


class TestUtils(unittest.TestCase):
    def test0_random(self):
        utils.random.seed("TestCase")
        self.assertNotEqual(utils.random.random(), utils.random.random())

        # make sure the seed is working
        utils.random.seed("TestCase")
        first = utils.random.random()
        utils.random.seed("TestCase")
        second = utils.random.random()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
