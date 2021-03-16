import socket
import logging
from datetime import datetime


class Server:
    def __init__(self):
        """Инициализация необходимых параметров"""
        self.users, self.cookies = {}, {}
        self.logger = self.get_logger()
        self.sock = socket.socket()
        self.port = 8080
        self.conn = None
        self.pass_key = 0
        self.k = 1

    def get_users(self):
        """Получение информации о предыдущих пользователях"""
        try:
            f = open("users.txt")
            for line in f:
                rr = line.split(":")
                spis = []
                spis.append(rr[1])
                spis.append(rr[2][:len(rr[2]) - 1])
                self.users[rr[0]] = spis
            f.close()
        except:
            self.users = {}

    def get_logger(self):
        """Получение логгера"""
        logger = logging.getLogger("server")
        logger.setLevel(logging.INFO)
        file_hanlder = logging.FileHandler("server.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_hanlder.setFormatter(formatter)
        logger.addHandler(file_hanlder)
        return logger

    def set_port(self):
        """Установление номера порта"""
        while True:
            port = input("Введите порт")
            if port == "":
                port = 8080
            elif port.isdigit() and 0 < int(port) < 65535:
                break
            else:
                print("Введите нормальный порт!")
        self.port = int(port)
        while self.port < 65535:
            if self.port >= 65535:
                raise AssertionError("Все порты заняты")
            try:
                self.sock.bind(('', int(self.port)))
                break
            except socket.error:
                self.port += 1

    def write_users(self):
        """Запись юзеров"""
        try:
            f = open("users.txt", "w")
            for line in self.users.items():
                f.write(str(line[0]) + ":" + str(line[1][0]) + ":" + str(line[1][1]) + "\n")
            f.close()
        except:
            pass

    def write_cookies(self):
        """Запись кукис"""
        try:
            f = open(f"{datetime.now().date()}.txt", "w+")
            for line in self.cookies.items():
                f.write(str(line[0]) + ":" + str(line[1][0]) + ":" + str(line[1][1]) + "\n")
            f.close()
        except:
            pass

    def listen(self):
        """Рабочая функция сервера"""
        while 1:
            self.write_users()
            self.write_cookies()
            if self.k == 1:
                self.conn, addr = self.sock.accept()
                user_port = addr[0]
                if user_port in self.users:
                    self.conn.send("SERVER: Привет, ".encode() + self.users[user_port][0].encode() + ". Введите пароль:".encode())

                else:
                    self.conn.send("SERVER: Привет! Придумайте имя и пароль, введите их через пробел:".encode())
                self.logger.info(f'Клиент {str(addr)} подключен')
                print(f'Клиент {str(addr)} подключен')
                self.k = 0
            else:
                try:
                    data = self.conn.recv(1024)
                    if not data:
                        self.logger.info("Отключение клиента...")
                        print("Клиент отключился")
                        self.k = 1
                        self.pass_key = 0
                        self.conn.close()
                    elif self.pass_key == 0:
                        if user_port in self.users:
                            if str(data.decode()[9:]) == self.users[addr[0]][1]:
                                self.conn.send("SERVER: Пароль верен".encode())
                                self.pass_key = 1
                            else:
                                self.pass_key = 0
                                self.k = 1
                                self.conn.send("SERVER: Пароль неверен".encode())
                                self.conn.close()
                        else:
                            info = str(data.decode())[9:]
                            r = []
                            try:
                                r.append(info.split()[0])
                                r.append(info.split()[1])
                                self.users[addr[0]] = r
                                print("Новый пользователь " + str(info.split()[0]))
                                self.conn.send("SERVER: Пользователь зарегистрирован".encode())
                                self.pass_key = 1
                            except IndexError:
                                self.conn.send("SERVER: Введите имя и пароль через пробел!".encode())
                                self.pass_key = 0

                    else:
                        key = input("Если хотите выключить сервер, то напишите что-то кроме enter.")
                        info = data.decode()[9:]
                        cook = []
                        cook.append(data.decode()[9:])
                        cook.append(datetime.now())
                        self.cookies[addr[1]] = cook
                        print("Данные получены: " + info)
                        print(f"Длина данных: {len(data.decode()[9:])}")
                        self.logger.info("Данные получены:")
                        self.conn.send("SERVER: ".encode() + info.upper().encode())
                        self.logger.info("Отправка данных клиенту...")
                        if key != "":
                            break
                except ConnectionError:
                    print("Клиент отключен")
                    self.logger.info("Отключение клиента...")
                    self.k = 1
                    self.pass_key = 0
                    self.conn.close()

    def online(self):
        """Основная функция для работы сервера"""
        self.get_users()
        self.set_port()
        print(f"Инициализированы пользователи: {self.users}")
        print("Сервер запущен!")
        self.logger.info("Сервер запущен!")
        self.logger.info(f'Начало прослушивание порта {str(self.port)}')
        self.sock.listen(1)
        self.listen()
        self.logger.info("Соединение закрыто!")
        print("Закрыли соединение")

        self.logger.info("Остановка сервера...")
        self.conn.send("SERVER: ".encode() + "отключение...".encode())
        self.conn.close()
        self.sock.close()


def main():
    server = Server()
    server.online()


if __name__ == "__main__":
    main()
