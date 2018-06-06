# -*- coding: utf-8 -*-
__author__ = 'vden'
import numpy as np




class FibonacciHelper():

    def __init__(self, generator):
        self.generator = generator

    def number(self, n):
        fib_n = np.linalg.matrix_power(
            np.array([[1,1], [1,0]], dtype='O'),
            n
        )[1,0]
        return fib_n


