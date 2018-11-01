__author__ = 'vden'

class Table_points_index_gist:

    def __init__(self, id=None, p_point_x=None, p_point_y=None):
        self.id = id
        self.p_point_x = p_point_x
        self.p_point_y = p_point_y


    def __repr__(self):
        return "%s,%s,%s" % (self.id, self.p_point_x, self.p_point_y)

    def __eq__(self, other):
        return (self.id == other.id and self.p_point_x == other.p_point_x and self.p_point_y == other.p_point_y )
