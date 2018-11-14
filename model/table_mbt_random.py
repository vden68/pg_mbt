__author__ = 'vden'

class Table_mbt_random:

    def __init__(self, fib_number=None, p_point_x=None, p_point_y=None):
        self.fib_number = fib_number
        self.p_point_x = p_point_x
        self.p_point_y = p_point_y


    def __repr__(self):
        return "%s,%s,%s" % (self.fib_number, self.p_point_x, self.p_point_y)

    def __eq__(self, other):
        return (self.fib_number==other.fib_number and self.p_point_x==other.p_point_x
                and self.p_point_y==other.p_point_y )
