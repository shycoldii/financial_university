import socket
import time


def send_file(name, sock):
    sock.send(f'send {name}'.encode())
    with open(name, 'r') as file:
        text = file.read()
    sock.send(str(len(text)).encode())
    sock.send(text.encode())
    return


def new_user(name, sock):
    sock.send(name.encode())
    flag = sock.recv(1024).decode()
    if int(flag):
        password = 'rr'
        sock.send(password.encode())
    else:
        flag2 = 1
        sock.send(str(flag2).encode())
        old_user(name, sock)


def old_user(name, sock):
    sock.send(name.encode())
    flag = sock.recv(1024).decode()
    if int(flag):
        password = 'rr'
        sock.send(password.encode())
        flag = sock.recv(1024).decode()


def login(sock):
    sock.send('1'.encode())
    new_user('rr', sock)


def testing():
    HOST = '127.0.0.1'
    PORT = 8080
    name = "rr"
    sock = socket.socket()
    sock.connect((HOST, PORT))

    login(sock)
    data = (sock.recv(1024).decode())
    if data != f'Hello, {name}':
        return "Ошибка в создании нового пользователя"

    request = 'pwd'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    if answer != f"\\{name}":
        return "Ошибка в pwd"

    def send_file(name, sock):
        """Отправялет файл на сервер"""

        with open(name, 'r') as file:
            text = file.read()

        sock.send(f'send {name}'.encode())
        print(str(len(text)))
        sock.send(str(len(text)).encode())
        print(text)
        time.sleep(1)
        sock.send(text.encode())
        return

    request = 'mkdir test'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    if answer != "Folder test successfully created":
        return "Ошибка в mkdir"

    # ls
    request = 'ls'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    if answer != "test":
        return "Ошибка в ls"

    # cd
    request = 'cd test'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    if answer != "Current directory: \\rr\\test":
        return "Ошибка в cd"
    request = 'pwd'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    if answer != "\\rr\\test":
        return "Ошибка в cd"

    # send
    name = "fff.txt"
    send_file(name,sock)
    answer = sock.recv(1024).decode()
    if answer != "file received fff.txt":
        return "Ошибка в send"


    # cd ..
    request = 'cd ..'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    print(answer)
    if not answer.startswith("Current directory"):
        print(answer)
        return "Ошибка в cd.."

    # rmdir
    request = 'rmdir test'
    sock.send(request.encode())
    answer = sock.recv(1024).decode()
    if answer != "Folder test successfully deleted":
        return "Ошибка в rmdir"

    # exit
    sock.close()



print(testing())