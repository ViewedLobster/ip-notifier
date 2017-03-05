import socket
import threading


class Notify_server:

    def __init__(self):

        self.server_socket = socket.socket()

        addr = ("localhost", 12345)

        self.server_socket.bind(addr)
        self.server_socket.listen()
   

    def start_server(self):

        done = False

        while not done:
            (new_conn, new_conn_address) = self.server_socket.accept()
            print("New connection from: ", new_conn_address)

            conn_handler = Connection_handler(new_conn)
            new_thread = threading.Thread(target=conn_handler)
            new_thread.start()


class Connection_handler:

    def __init__(self, connection):
        self.connection = connection

    def __call__(self):

        while True:
            s = self.connection.recv(1024)
            if s == b'':
                break
            print(s)




a = Notify_server()
a.start_server()
