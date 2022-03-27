import unittest
import painter


class TestPainterMethod(unittest.TestCase):
    def test_matrix(self):
        width = 24
        height = 24
        blueprints = { 'shape': 'blueprints/types/pug/shape/shape.csv' }
        out = painter.draw(width, height, blueprints, painter.PARETTO)
        self.assertTupleEqual(out.shape, (24,24,3))


if __name__ == '__main__':
    unittest.main()
