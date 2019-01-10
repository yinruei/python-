class PingPongParent:
    pass

class Ping(PingPongParent):
    def __init__(self, pong):
        self.pong = pong
    
class Pong(PingPongParent):
    def __init__(self, pings=None):
        if pings is  None:
            self.pings = []
        else:
            self.pings = pings
    
    def add_ping(self, ping):
        self.pings.append(ping)

pong = Pong()
print(pong)
ping = Ping(pong)
print(ping)
pong.add_ping(ping)