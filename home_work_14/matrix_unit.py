from home_work_11.matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.test_matrix_1 = Matrix([[1, 2, 3], [6, 4, 5]])
        self.test_matrix_2 = Matrix([[7, 8, 9], [5, 1, 7]])
        self.test_matrix_3 = Matrix([[11, 22, 33], [61, 43, 54]])
        self.test_matrix_4 = Matrix([100, 220, 313])

    def test_mul(self):
        self.assertEqual(self.test_matrix_2 * self.test_matrix_1, Matrix([[50, 119], [28, 69]]))

    def test_mul_2(self):
        self.assertTrue(self.test_matrix_2 * self.test_matrix_1 == Matrix([[50, 119], [28, 69]]))

    def test_mul_3(self):
        self.assertFalse(self.test_matrix_1 * self.test_matrix_2 == Matrix([[500, 119], [28, 690]]))

    def test_sum_1(self):
        self.assertEqual(self.test_matrix_3 + self.test_matrix_1, Matrix([[12, 24, 36], [67, 47, 59]]))

    def test_sum_error(self):
        self.assertTrue(self.test_matrix_2 + self.test_matrix_4 == None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
