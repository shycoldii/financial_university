import socket, threading

def accept_client():
    while True:
        #accept
        cli_sock, cli_add = ser_sock.accept()
        CONNECTION_LIST.append(cli_sock)
        thread_client = threading.Thread(target = broadcast_usr, args=[cli_sock])
        thread_client.start()

def broadcast_usr(cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
               b_usr(cli_sock, data)
        except Exception as x:
            pass

def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)
if __name__ == "__main__":
    CONNECTION_LIST = []
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind
    HOST = 'localhost'
    PORT = 5060
    ser_sock.bind((HOST, PORT))
    # listen
    ser_sock.listen(1)
    print('Chat server started on port : ' + str(PORT))
    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()