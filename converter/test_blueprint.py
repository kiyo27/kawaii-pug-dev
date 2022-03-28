import unittest
import blueprint as bp

class TestPugMethods(unittest.TestCase):
    def test_pug(self):
        p = bp.Pug()

    def test_androidpug(self):
        ap = bp.AndroidPug()
        print(ap.attributes)


    def test_anonypug(self):
        ap = bp.AnonyPug()
        self.assertIsInstance(ap, bp.AnonyPug)


if __name__ == '__main__':
    unittest.main()
