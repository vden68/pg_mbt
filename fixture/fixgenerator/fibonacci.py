# -*- coding: utf-8 -*-
__author__ = 'vden'
import numpy as np

i_numbers_list=None


class FibonacciHelper():

    def __init__(self, generator):
        self.generator = generator


    def number(self, n):
        fib_n = np.linalg.matrix_power(
            np.array([[1,1], [1,0]], dtype='O'),
            n
        )[1,0]
        return fib_n


    def numbers_list(self):

        global i_numbers_list

        if i_numbers_list is None:

            i_numbers_list=[]
            i_fib = 1
            fib = self.number(i_fib)

            while fib < 9223372036854775807:
                i_numbers_list.append(fib)
                i_fib = i_fib + 1
                fib = self.number(i_fib)

        return i_numbers_list


