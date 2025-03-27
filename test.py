import unittest
import numpy as np
from helper import multiply, transpose, calcEigenvalues, calcEigenvectors, calcSigma, createSVD, createPCA

class TestMatrixFunctions(unittest.TestCase):
    
    def setUp(self):
        self.A = np.array([[1, 2], [3, 4]])
        self.B = np.array([[2, 0], [1, 2]])
        self.rect = np.array([[126, 78],
                            [128, 80],
                            [128, 82],
                            [130, 82],
                            [130, 84],
                            [132, 86]])

    def test_multiply(self):
        expected = np.array([[4, 4], [10, 8]])
        np.testing.assert_array_almost_equal(multiply(self.A, self.B), expected)
        expected = np.matmul(self.rect, self.B)
        np.testing.assert_array_almost_equal(multiply(self.rect, self.B), expected)
    
    def test_transpose(self):
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_almost_equal(transpose(self.A), expected)
        expected = self.rect.T 
        np.testing.assert_array_almost_equal(transpose(self.rect), expected)

    def test_calcSigma(self):
        eigenvalues = calcEigenvalues(self.A)
        expected = np.diag([np.sqrt(eigenvalues[i]) if i < len(eigenvalues) else 0 for i in range(len(self.A))])
        np.testing.assert_array_almost_equal(calcSigma(self.A, eigenvalues), expected)
    
    def test_createSVD(self):
        U, Sigma, V_transpose = createSVD(self.A)
        U_np, Sigma_np, V_np = np.linalg.svd(self.A)
        Sigma_np_matrix = np.zeros_like(self.A, dtype=float)
        np.fill_diagonal(Sigma_np_matrix, Sigma_np)
        np.testing.assert_array_almost_equal(np.abs(U), np.abs(U_np))
        np.testing.assert_array_almost_equal(Sigma, Sigma_np_matrix)
        np.testing.assert_array_almost_equal(np.abs(V_transpose), np.abs(V_np))
    
    def test_createPCA(self):
        pcs, significance = createPCA(self.A, 2)
        self.assertEqual(pcs.shape[1], 2)
        self.assertAlmostEqual(sum(significance), 1.0, places=5)
        pcs, significance = createPCA(self.rect, 2)
        self.assertEqual(pcs.shape[1], 2)
        self.assertAlmostEqual(sum(significance), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
