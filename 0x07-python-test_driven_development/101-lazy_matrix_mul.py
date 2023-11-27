#!/usr/bin/python3

"""
    lazy_matrix_mul modeule
    provide a function that multiplies two matrix
    with the numpy module
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 gi ven matrix
        Args:
            m_a(matrix)
            m_b(matrix)
    """

    return numpy.matmul(m_a, m_b)
