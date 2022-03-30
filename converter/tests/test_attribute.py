import unittest
import blueprint as bp

class TestAttrubuteMethods(unittest.TestCase):
    def test_something(self):
        d = {"face":{"group":"facemask","name":"anonymous"}}
        a = bp.Face(**d)
        print(a.path)


if __name__ == '__main__':
    unittest.main()
