import socket
from FTP_5_lab.commands import Command
def set_new_user(name,sock):
    if int(preprocess(sock,name)):
        while True:
            print("Type password")
            password = input()
            print("Repeat password")
            password2 = input()
            if password == password2:
                break
        sock.send(password.encode())
    else:
        print("Name is already exist")
        print("For login with this name type 1")
        print("Another name - type 0")
        flag2 = input()
        while flag2!="0" or flag2!="1":
            flag2=input()
        sock.send(str(flag2).encode())
        if flag2:
            set_old_user(name,sock)
        else:
            name = input("Type your name: ")
            set_new_user(name,sock)


def set_old_user(name,sock):
    if int(preprocess(sock,name)):
        while True:
            password = input("Password: ")
            sock.send(password.encode())
            flag = sock.recv(1024).decode()
            if not int(flag):
                break
    else:
        print("Name wasn't found")
        print("For registration type 1")
        print("Another name type 0")
        flag2=""
        while flag2!="0" or flag2!="1":
            flag2 = input("Type 1 or 0")
        sock.send(flag2.encode())
        if int(flag2):
            set_new_user(name,sock)
        else:
            name = input("Type your name: ")
            set_old_user(name,sock)

def preprocess(sock,name):
    sock.send(name.encode())
    flag = sock.recv(1024).decode()
    return flag

def get_login(sock):
    while True:
        data = input("Write login or reg").lower()
        if data == 'reg':
            sock.send('1'.encode())
            print("Write your name: ")
            name = input()
            set_new_user(name,sock)
            break
        elif data == 'login':
            sock.send('0'.encode())
            name = input('Write your name: ')
            set_old_user(name,sock)
            break
        else:
            print("Incorrect input. Try again!")
def main():
    HOST = 'localhost'
    PORT = 8080
    sock = socket.socket()
    try:
        sock.connect((HOST, PORT))
    except:
        print("404")
        return
    print(f"Successful connection with {HOST} {PORT}")
    get_login(sock)
    print(sock.recv(1024).decode())

    while True:
        try:
            request = input(">")
            if request == 'exit':
                break
            elif request.split()[0] == 'send':
                Command().send_file_to_server(request.split()[1], sock)
                answer = sock.recv(1024).decode()
            elif request.split()[0] == 'recv':
                answer =  Command().recv_file_from_server(request.split()[1], sock)
                if answer!="Syntax error or action isn't available":
                    answer = sock.recv(1024).decode()

            else:
                sock.send(request.encode())
                answer = sock.recv(1024).decode()
            print(answer)
        except Exception as e:
            print(e)

    sock.close()

if __name__ == "__main__":
    main()
