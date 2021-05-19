import random


class Cipher:
    """
    Класс для создания протокола Диффи-Хеллмана
    """
    def __init__(self,g=None,p=None,private=None):
        self.g = g
        self.p = p
        self.private = private
    def check_key(self):
        """
        Функция для сверки текущих ключей из файла для доступа клиенту
        """
        if self.g==None:
            return False
        try:
            with open('keys.txt', 'r') as file:
                for line in file:
                    if int(line) == self.g:
                        return True
                return False
        except:
            return False

    def generate_B(self):
        return self.g ** self.private % self.p

    def generate_K(self, A):
        self.K = A ** self.private % self.p
        return self.K

    def crypt(self,message,mode):
        """
        Используется для шифрования и дешифрования
        """
        key = chr((self.K + 2) % 65536) + chr((self.K + 2) % 65536) + chr((self.K + 5) % 65536)
        keys = ''
        while len(keys) != len(message):
            for i in key:
                if len(keys) != len(message):
                    keys = keys + i
                else:
                    break
        new_msg = ''
        for i in range(len(keys)):
            if mode=="E":
                i = (ord(message[i]) - ord(keys[i])) % 65536
            else:
                i = (ord(message[i]) + ord(keys[i])) % 65536
            new_msg = new_msg + chr(i)
        return new_msg

    def create_bunch(self):
        """
        Создание клиентом ключей
        """
        self.private = random.randint(1, 200)
        self.g = int(input('Enter your public key (1, 999)>'))
        self.p = int(input('Enter your  key (1, 999)>'))

    def read_ready_keys(self):
        """
        Чтение готовых публичных ключей из файла
        """
        try:
            with open('ready_keys.txt', 'r') as file:
                for line in file:
                    if len(line)!=0:
                        self.g = int(line.split()[0])
                        self.p = int(line.split()[1])
                        self.private = random.randint(1, 200)
                        return True
                return False

        except FileNotFoundError:
            return False




