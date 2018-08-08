__author__ = 'vden'

class Table_fibonacci_number:

    def __init__(self, id=None, fib_number=None):
        self.id = id
        self.fib_number = fib_number


    def __repr__(self):
        return "%s,%s" % (self.id, self.fib_number)
