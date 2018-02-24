#!python
import unittest
from recognizer.tools import *


class TestToolsFunctions(unittest.TestCase):

    def test_read_line(self):
        line = "1,0,1,2,3,4"
        self.assertEqual([1, 0, 1, 2, 3, 4], read_line_image(line))

    def test_transform_array_to_labeled_matrix(self):
        expected_label = 0
        expected_matrix = np.asmatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        array_image = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        output_matrix, output_label = transform_array_to_labeled_matrix(array_image, 3)

        self.assertEqual(expected_label, output_label)
        self.assertTrue((expected_matrix == output_matrix).all)


if __name__ == '__main__':
    unittest.main()
