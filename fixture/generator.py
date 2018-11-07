__author__ = 'vden'

from fixture.fixgenerator.fibonacci import FibonacciHelper
from fixture.fixgenerator.p_points import PointsHelper



class Generatorfixture:

    def __init__(self):
        self.fibonacci = FibonacciHelper(self)
        self.p_points = PointsHelper(self)



    def destroy(self):
        pass


