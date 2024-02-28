import socket

class TCPSocketContextManager:
    def __init__(self, server_address, message):
        self.server_address = server_address
        self.message = message
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self):
        print('connecting to {} port {}'.format(*self.server_address))
        self.sock.connect(self.server_address)
        print('sending {!r}'.format(self.message))
        self.sock.sendall(self.message)
        return self.sock

    def __exit__(self, exc_type, exc_value, traceback):
        print('closing socket')
        self.sock.close()
        if exc_type:
            print(f'Exceptie: {exc_type}, {exc_value}')

# Usage example:
server_address = ('localhost', 10000)
message = b'Asta e mesajul. O sa fie repetat.'

with TCPSocketContextManager(server_address, message) as sock:
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))
