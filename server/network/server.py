import socket



class Server:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        self.listener.setblocking(False)
        self.connection = None

    def start(self):
        self.listener.bind((self.host, self.port))
        self.listener.listen(1)
        


    
