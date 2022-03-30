import unittest
import blueprint as bp

class TestPugMethods(unittest.TestCase):
    def test_pug(self):
        p = bp.Character.get_factory('Pug')
        d = {}
        p.create(**d)
        self.assertEqual(p.attributes.mouth, None)

    def test_anonypug(self):
        p = bp.Character.get_factory('AnonyPug')
        d = {'attributes':{'mouth':'cigarette'}}
        p.create(**d)
        self.assertEqual(p.attributes.mouth, 'cigarette')
