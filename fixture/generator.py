__author__ = 'vden'

from fixture.fixgenerator.fibonacci import FibonacciHelper



class Generatorfixture:

    def __init__(self):
        self.fibonacci = FibonacciHelper(self)



    def destroy(self):
        pass


