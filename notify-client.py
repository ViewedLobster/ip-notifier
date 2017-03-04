import socket


ip_address = "localhost"
port = 12345

def notifier():
    
    addr = (ip_address, port)
    new_conn = socket.create_connection(addr)

    new_conn.send()
    new_conn.close()

notifier()


