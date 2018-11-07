# -*- coding: utf-8 -*-
__author__ = 'vden'

import random
from model.basic_tables.table_points_index_gist import Table_points_index_gist

class PointsHelper():

    def __init__(self, generator):
        self.generator = generator

    def g_points(self, coumt_points=None):

        range_count_points = range(coumt_points)
        x = [random.uniform(-100, 100) for i in range_count_points]
        y = [random.uniform(-100, 100) for i in range_count_points]

        list_points=[]
        for i in range_count_points:
            list_points.append(Table_points_index_gist(p_point_x=round(x[i], 2), p_point_y=round(y[i],2)))

        return list_points





