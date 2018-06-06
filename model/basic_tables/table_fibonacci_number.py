__author__ = 'vden'

class Table_fibonacci_number:

    def __init__(self, id=None, fib_number=None, test_start_timestamp=None):
        self.id = id
        self.fib_number = fib_number
        self.test_start_timestamp = test_start_timestamp


    def __repr__(self):
        return "%s,%s,%s" % (self.id, self.fib_number, self.test_start_timestamp)
