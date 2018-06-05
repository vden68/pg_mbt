__author__ = 'vden'

class Mbt_hosts:

    def __init__(self, host=None, port=None, write=None, read=None):
        self.host = host
        self.port = port
        self.write = write
        self.read = read


    def __repr__(self):
        return "%s,%s,%s,%s" % (self.host, self.port, self.write, self.read)
