from twisted.internet.protocol import Protocol, connectionDone
from twisted.python import failure


class Echo(Protocol):
    def __init__(self, factory):
        self.factory=factory
    def dataReceived(self, data: bytes):
        self.transport.write(data)
    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols+1
        self.transport.write()
        'Weleocme There are currently %d open connections.\n'%(self.factory.numProtocols)
    def connectionLost(self, reason: failure.Failure = connectionDone):
        self.factory.numProtocols = self.factory.numProtocols-1
