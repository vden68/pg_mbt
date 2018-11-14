__author__ = 'vden'

from fixture.fixgenerator.fibonacci import FibonacciHelper
from fixture.fixgenerator.p_points import PointsHelper
from fixture.fixgenerator.mbt_random import MbtRandomHelper



class Generatorfixture:

    def __init__(self):
        self.fibonacci = FibonacciHelper(self)
        self.p_points = PointsHelper(self)
        self.mbt_random = MbtRandomHelper(self)



    def destroy(self):
        pass


