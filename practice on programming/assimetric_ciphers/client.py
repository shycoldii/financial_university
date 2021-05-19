import socket
import time

from SHIVR_ASSIM.cipher import Cipher

HOST = 'localhost'
PORT = 8080

def generate_port(K):
   """
        Используется для создания нового порта для общения
   """
   global PORT
   NEW_PORT = PORT + (PORT - K)%K
   try:
       if int(NEW_PORT)<9999:
           return NEW_PORT
       else:
           return -1
   except:
       return -1
try:
    sock = socket.socket()
    sock.connect((HOST, PORT))
    cipher = Cipher()
    if not cipher.read_ready_keys():
        cipher.create_bunch()
    sock.send((str(cipher.g)+" "+str(cipher.p)).encode())
    if sock.recv(1024).decode() == "Access is allowed":
        server_key_partial = int(sock.recv(1024).decode())
        client_partial_key = cipher.generate_B()
        sock.send(str(client_partial_key).encode())
        cipher.generate_K(server_key_partial)
        NEWPORT = generate_port(cipher.K)
        if NEWPORT == -1:
            print("Incorrect port!")
            sock.close()
        else:
            sock.send((cipher.crypt("Connection", "E") +" "+ cipher.crypt(str(NEWPORT), "E")).encode())
            sock.close()
            sock = socket.socket()
            time.sleep(5)
            sock.connect((HOST, NEWPORT))
            while True:
                msg = input(">")
                if msg.lower()=="exit":
                    break
                sock.send((cipher.crypt(msg, "E")).encode())
                ans = sock.recv(1024).decode()
                print("response: "+cipher.crypt(ans,"D"))

    else:
        print("Access not allowed")
        sock.close()

except ZeroDivisionError as e:
    print(e)