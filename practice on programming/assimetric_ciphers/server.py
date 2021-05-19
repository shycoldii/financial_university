import random
import socket
from multiprocessing import Pool
from SHIVR_ASSIM.cipher import Cipher

def get_ports(args):
    """
    Используется для создания ПУЛА портов и последующего общения с клиентами
    args - номер порта и экземпляр класса cipher
    """
    port, cipher = args
    sock = socket.socket()
    sock.bind(('localhost', port))
    print(f'Listening {port}...')
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        try:
            msg = conn.recv(2024).decode()
            encoded_msg = cipher.crypt(msg, "D")
            print(f'Encrypt message: {msg} \nDecrypt message: {encoded_msg}\n')
            conn.send(str(cipher.crypt(str(encoded_msg).upper(),"E")).encode())
        except ConnectionError as e:
            print(e)
            conn.close()
            break

if __name__=="__main__":
    HOST = 'localhost'
    PORT = 8080
    ports = []
    ports.append(PORT)
    try:
        print(f'Listening {PORT}...')
        sock = socket.socket()
        sock.bind((HOST, PORT))
        sock.listen(1)
        conn, addr = sock.accept()
        answer = conn.recv(2054).decode().split()
        cipher = Cipher(int(answer[0]), int(answer[1]), random.randint(1, 200))
        if cipher.check_key():
            conn.send("Access is allowed".encode())
            #send B
            conn.send(str(cipher.generate_B()).encode())
            A = int(conn.recv(1024).decode())
            #get A
            cipher.generate_K(A)
            msg = conn.recv(2024).decode().split()
            conn.close()
            sock.close()
            ports.append(int(cipher.crypt(msg[1], "D")))
            with Pool() as p:
                print(p.map(get_ports, zip(ports, [cipher]*len(ports))))

        else:
            conn.close()

    except ZeroDivisionError as e:
        print(e)
    except ConnectionError as e:
        print(e)
        sock.close()