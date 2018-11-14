# -*- coding: utf-8 -*-
__author__ = 'vden'

from model.table_mbt_random import Table_mbt_random


class MbtRandomHelper():

    def __init__(self, generator):
        self.generator = generator

    def random_generator(self):
        fibonacci_list = self.generator.fibonacci.numbers_list()
        p_points_list = self.generator.p_points.g_points(coumt_points=1000)

        mbt_random_list=[]
        f_l = 0
        for p in p_points_list:
            mbt_random_list.append(Table_mbt_random(fib_number=fibonacci_list[f_l],
                                                    p_point_x=p.p_point_x, p_point_y=p.p_point_y))
            if f_l==91:
                f_l = 0
            else:
                f_l += 1

        return mbt_random_list






