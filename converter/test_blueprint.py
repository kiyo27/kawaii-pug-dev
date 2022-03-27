import unittest
import blueprint as bp

class TestPugMethods(unittest.TestCase):
    def test_pug(self):
        p = bp.Pug()
        self.assertEqual(
            'blueprints/types/pug/shape_shape.csv',
            p.blueprints['shape_shape']
        )

    def test_androidpug(self):
        p = bp.AndroidPug()
        #print(p.blueprints)

    def test_reflection(self):
        p = bp.Pug()
        p.add_attribute('eyes')
        p.blueprints['eyes']
        self.assertRaises(KeyError, p.add_attribute, 'keyerror')

    def test_csv(self):
        print(bp.eyes())

    def test_anonypug(self):
        p = bp.AnonyPug()



if __name__ == '__main__':
    unittest.main()
