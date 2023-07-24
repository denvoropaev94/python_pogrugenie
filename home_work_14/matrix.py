from home_work_11.matrix import Matrix


def test_matrix():
    """
    >>> print(repr(Matrix([[1, 2, 3], [6, 4, 5]])))
    Matrix([[1, 2, 3], [6, 4, 5]])
    >>> print(repr(Matrix([[1, 2, 3], [6, 4, 5]]) * Matrix([[7, 8, 9], [5, 1, 7]])))
    Matrix([[50, 28], [119, 69]])
    >>> print(repr(Matrix([[7, 8, 9], [5, 1, 7]]) + Matrix([[1, 2, 3], [6, 4, 5]])))
    Matrix([[8, 10, 12], [11, 5, 12]])
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
