__author__ = 'vden'

class Mbt_hosts:

    def __init__(self, host=None, node_id=None, port=None, write=None, read=None, enabled=None):
        self.host = host
        self.node_id = node_id
        self.port = port
        self.write = write
        self.read = read
        self.enabled = enabled


    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.host, self.node_id, self.port, self.write, self.read, self.enabled)
