import unittest
from blueprint import Pug, AndroidPug

class TestPugMethods(unittest.TestCase):
    def test_pug(self):
        p = Pug()
        self.assertEqual(
            'blueprints/types/pug/shape/shape.csv',
            p.blueprints['shape']
        )

    def test_androidpug(self):
        p = AndroidPug()
        print(p.blueprints)


if __name__ == '__main__':
    unittest.main()
