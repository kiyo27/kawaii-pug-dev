import unittest

import blueprint as bp


class TestPugMethods(unittest.TestCase):
    def test_pug(self):
        p = bp.Character.get_factory("Pug")
        d = {}
        p.create(**d)

    def test_anonypug(self):
        p = bp.Character.get_factory("AnonyPug")
        d = {"attributes": {"mouth": "cigarette"}}
        p.create(**d)
        self.assertEqual(p.attributes.mouth, "cigarette")

    def test_sleepingpug(self):
        p = bp.Character.get_factory("SleepingPug")
        d = {}
        p.create(**d)
        self.assertEqual(p.shape.eyes, "blueprints/base/shape/eyes/sleeping.csv")

    def test_puginstance(self):
        p = bp.Character.get_factory("Pug")
        p.create()
        ap = bp.Character.get_factory("AnonyPug")
        ap.create()
        self.assertIsNot(p, ap)

    def test_kwargs(self):
        p1 = bp.Character.get_factory("AnonyPug")
        p1.create()
        p2 = bp.Character.get_factory("AnonyPug")
        p2.create()
        print(p1 == p2)
