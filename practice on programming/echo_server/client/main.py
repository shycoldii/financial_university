from socket import *

class Client:
    def __init__(self):
        self.sock = socket(SOCK_DGRAM)
        self.port = self.get_port()
        self.host = self.get_host()
        self.pass_key = 0

    def get_port(self):
        """Получение порта"""
        while True:
            port = input("Введите порт")
            if port == "":
                port = 8080
            elif port.isdigit() and 0 < int(port) < 65535:
                break
            else:
                print("Введите нормальный порт!")
        return int(port)


    def get_host(self):
        """Получение хоста"""
        while True:
            host = input("Введите хост")
            if host == "":
                host = "localhost"
            try:
                print(host, self.port)
                self.sock.connect((host, int(self.port)))
                break
            except Exception as e:
                print(e)
                print("Не удалось подключиться :(")
        return host
    def listen(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print("Приняты данные от сервера: " + data.decode()[8:])
                    if data.decode()[8:] == "Пароль неверен":
                        break
                    print(f"Длина данных: {len(data.decode()[8:])}")
                else:
                    print("Сервер разорвал соединение")
                    break
                key = input("Введите строку")
                if key == "exit":
                    break
                self.sock.send("CLIENT 1:".encode() + key.encode())
            except:
                break
    def online(self):
        print("Соединено с сервером!")
        self.listen()
        print("Разрыв соединения...")
        self.sock.close()


if __name__ == "__main__":
    client = Client()
    client.online()


