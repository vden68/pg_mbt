__author__ = 'vden'

class Check_table_fibonacci_number:

    def __init__(self, fib_number=None, count=None):
        self.fib_number = fib_number
        self.count = count


    def __repr__(self):
        return "%s,%s" % (self.fib_number, self.count)

    def __eq__(self, other):
        return (self.fib_number == other.fib_number and self.count == other.count)
