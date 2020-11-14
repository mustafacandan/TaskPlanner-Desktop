import weakref

class Connection:
    instances = weakref.WeakSet()

    def __init__(self, ip, port, token=None):
        self.ip = ip
        self.port = port
        self.token = token
        Connection.instances.add(self)

    @classmethod
    def get_all(cls):
        return list(Connection.instances)