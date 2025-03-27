import numpy as np
import csv

def main():
    '''
    Main function to use for personal testing. 
    Nothing in this function will affect the autotests.
    '''
    pass


def multiply(A, B):
    '''
    Function that takes two compatible matrices and multiplies them together.
    param A: matrix in dimensions m by n
    param B: matrix in dimensions n by m
    return: product of the matrices
    '''
    pass


def transpose(A):
    '''
    Creates the transpose of a matrix.
    param A: matrix in dimensions m by n
    return: transpose of a A (n by m)
    '''
    pass


def calcEigenvalues(A):
    '''
    Calculates all of the eigenvalues of a matrix.
    param A: matrix of dimension m by n
    return: list of eigenvalues in desending order
    '''
    eigenvalues, Eigenvectors = np.linalg.eig(A)
    return sorted(eigenvalues)


def calcEigenvectors(A):
    '''
    Calculates all of the eigenvalues of a matrix
    param A: matrix of dimension m by n
    return: orthogonal matrix of eigenvalues
    '''
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvectors


def calcSigma(A, eigenvalues):
    '''
    Creats Sigma matrix from the original matrix and eigenvalues.
    param A: matrix of dimension m by n
    param eigenvales: list of eigenvales in decending order
    return: Sigma matrix of dimension m by n
    '''
    pass


def createSVD(A):
    '''
    Creates the SVD for A
    param A: matrix of dimension m by n
    return: matrix U (m by m)
    return: matrix Sigma (m by n)
    return: matrix V_transpose (n by n)
    '''
    pass
    

def createPCA(A, components):
    '''
    Create matrix of principle component vectors of matrix A.
    param A: matrix of dimension m by n
    param components: number of principle components desired
    return: matrix of principle componenents (components by n)
    '''
    pass



if __name__ == "__main__":
    main()