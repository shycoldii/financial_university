import os
import socket
import shutil

def pwd():
    if name == 'admin':
        return os.getcwd()
    return os.getcwd()[len(ROOTNAME):]


def ls():
    resp = ' '.join(os.listdir(os.getcwd()))
    if resp:
        return resp
    else:
        return "Folder is empty"


def cat(name):
    with open(name, 'r') as file:
        s = file.read()
        if s:
            return s
        else:
            return "File is empty"


def get_size(name):
    path = ROOTNAME + f'\\{name}'
    result = 0
    for directory, subdirectory, files in os.walk(path):
        if files:
            for file in files:
                path = directory + f'\\{file}'
                result += os.path.getsize(path)
    return result


def rm(name):
    os.remove(os.getcwd() + '\\' + name)
    return f'file {name} successfully deleted'


def send(name, conn, user):
    length = conn.recv(1024).decode()
    text = conn.recv(int(length)).decode()
    with open(name, 'w') as file:
        file.write(text)
    if user != 'admin':
        if get_size(user) > MAXSIZE:
            rm(name)
            return 'Insufficient disk space'
    return f'file received {name}'


def recv(name, conn):
    with open(name, 'r') as file:
        text = file.read()
    if text:
        conn.send(str(len(text)).encode())
        return f'Sent {name}'
    else:
        return "File or folder is empty"


def mkdir(name):
    os.mkdir(os.getcwd() + "\\" + name)
    return f'Folder {name} successfully created'


def rmdir(name):
    shutil.rmtree(os.getcwd() + '\\' + name)
    return f'Folder {name} successfully deleted'


def touch(name):
    with open(name, 'w'):
        pass
    return f'File {name} successfully created'


def cd(path):
    if path == '..':
        if os.getcwd() == home_directory:
            return 'You are in a root'
        directory = '\\'.join(os.getcwd().split('\\')[:-1])

    else:
        directory = '\\'.join(os.getcwd().split('\\')) + '\\' + path
    os.chdir(directory)
    return f'Current directory: {pwd()}'

def rename(name1, name2):
    os.rename(name1, name2)
    return f'File {name1} renamed to {name2}'


def process(req, args=None):
    dispatcher =  {'pwd':pwd, 'ls':ls, 'mkdir':mkdir,"recv": recv,"send": send,
                   "cd":cd,"rmdir":rmdir,"touch":touch,"cat":cat,"rename":rename,"rm":rm}
    try:
        if req in dispatcher:
            if args:
                return dispatcher[req](*args)
            else:
                return dispatcher[req]()

        return f"Command {req} not found"
    except Exception as e:
        print(e)
        return "Syntax error or action isn't available"

def get_users():
    try:
        open('users.txt', 'r')
    except FileNotFoundError:
        with open('users.txt', 'w'):
            pass
    with open('users.txt', 'r') as users:
        try:
            users = eval(users.read())
        except:
            return dict()
    return users

def get_args(request):
    if len(request) > 0:
        args = request[1:]
    else:
        args = None
    return args

def write_log(request):
    with open(LOG, 'a', encoding="UTF-8") as logs:
        print(request, file=logs)

def set_new_user(conn, user):
    name = conn.recv(1024).decode()
    if name not in USERS.keys():
        conn.send('1'.encode())
        password = conn.recv(1024).decode()
        user[name] = user.get(name, password)
        file =  'users.txt'
        with open(file, 'w') as users:
            print(user, file=users)
        path = ROOTNAME + '\\' + name
        os.mkdir(path)
        return name
    else:
        conn.send('0'.encode())
        flag2 = conn.recv(1024).decode()
        if int(flag2):
            name = set_old_user(conn, user)
            return name
        else:
            name = set_new_user(conn, user)
            return name
def set_old_user(conn, users):
    name = conn.recv(1024).decode()
    if name in users.keys():
        conn.send('1'.encode())
        passwd = users[name]
        while True:
            password = conn.recv(1024).decode()
            if passwd == password:
                conn.send('0'.encode())
                return name
            else:
                conn.send('1'.encode())
    else:
        conn.send('0'.encode())
        flag2 = conn.recv(1024).decode()
        if int(flag2):
            name = set_new_user(conn, users)
            return name
        else:
            name = set_old_user(conn, users)
            return name
#==========================================================================
ROOTNAME = os.path.join(os.getcwd(), 'files')
LOG = ROOTNAME + '\\log.txt'
PORT = 8080
MAXSIZE = 500
with open(LOG, 'a', encoding="UTF-8") as logs:
    print(f"Port {PORT} is listening now, maxsize = {MAXSIZE}", file=logs)
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
USERS = get_users()
USERS["admin"] = "test"
#==========================================================================
try:
    while True:
        home_directory = ROOTNAME
        conn, addr = sock.accept()
        try:
            write_log(f"Connection with {addr}")
            flag = int(conn.recv(1).decode())
            if flag:
                name = set_new_user(conn, USERS)
                write_log(f"User has registered: {name}")
            else:
                name = set_old_user(conn, USERS)
                write_log(f"User has entered: {name}")
            conn.send(f"Hello, {name}".encode())
            if name != "admin":
                home_directory += f'\\{name}'
            path = '\\'.join(home_directory.split('\\'))
            os.chdir(path)
            while True:
                    request = conn.recv(1024).decode()
                    write_log(request + " " + name)
                    if not request:
                        break
                    f = request.split()[0]
                    args = get_args(request.split())
                    if args:
                        if f in ["send", "recv"]:
                            args.append(conn)
                            if f == 'send':
                                args.append(name)
                        response = process(f, args)
                    else:
                        response = process(f)
                    print(response)
                    conn.send(response.encode())
            conn.close()
        except ConnectionError:
            print("Client didn't response")
            print("Break connection with "+addr[0])
            conn.close()
except KeyboardInterrupt:
    sock.close()