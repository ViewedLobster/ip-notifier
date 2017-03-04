import socket

def setup():

    server_socket = socket.socket()

    addr = ("localhost", 12345)

    server_socket.bind(addr)
    server_socket.listen()

    (new_conn, new_conn_address) = server_socket.accept()
    print("New connection from: ", new_conn_address)

    while True:
        s = new_conn.recv(1024)
        if s == b'':
            break
        print(s)

    


setup()

