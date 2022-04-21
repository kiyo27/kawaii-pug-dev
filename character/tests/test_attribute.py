import unittest
from character.types import Pug, SleepingPug


class TestAttrubuteMethods(unittest.TestCase):
    def test_optional_attribute(self):
        p = SleepingPug()
        attr = {"attributes": {"glasses": "horned-rim-glasses"}}
        p.create(1, **attr)


if __name__ == "__main__":
    unittest.main()
