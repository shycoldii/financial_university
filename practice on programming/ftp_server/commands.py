import time


class Command:
    @staticmethod
    def send_file_to_server(name, sock):
        """
        Отсылает файл на сервер
        """
        sock.send(f'send {name}'.encode())
        with open(name, 'r') as file:
            text = file.read()
        sock.send(str(len(text)).encode())
        time.sleep(1)
        sock.send(text.encode())
    @staticmethod
    def recv_file_from_server(name, sock):
        """
        Получает файл с сервера
        """
        sock.send(f'recv {name}'.encode())
        text = sock.recv(1024).decode()
        if text != "Syntax error or action isn't available":
            with open(name, 'w') as file:
                file.write(text)
        return text

