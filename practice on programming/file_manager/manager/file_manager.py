import os
import shutil


class FileManager:

    def __init__(self, home_dir):
        """
        :param home_dir: String
        :param help_text: String
        """
        self.home_dir = home_dir
        self.temp_dir = home_dir
        self.help_text = "goto [название директории] - смена директории на указанную \n" \
                         "goto.. - подняться выше по иерархии\n" \
                         "info - содержимое директории\n" \
                         "help - вывод доступных команд\n" \
                         "delete [name] - удаление папки или файла с указанным именем\n" \
                         "make [name] - создание пустого файла с указанным именем\n" \
                         "write [name] [info] - запись в файл указанное содержание\n" \
                         "read [name] - вывод содержимого указанного файла\n" \
                         "copy [current_name] [new_name] - копирования файла current_name в новый с " \
                         "именем new_name\n" \
                         "move [current_name] [new_name] - перемещение файла current_name в директорию" \
                         " new_name\n" \
                         "rename [current_name] [new_name] - переименовывание файла\n" \
                         "create [name] - создание новой директории\n"


    def help(self):
        """
        Метод вывода списка команд
        """
        print(self.help_text)

    def is_exist(self):
        """
        Возвращает статус существования стартовой директории (можно ли с ней начать работу)
        :return: boolean
        """
        if os.path.exists(self.home_dir) and os.path.isdir(self.home_dir):
            return True
        return False

    def info(self):
        """
        Вывода содержимого директории (как ls)
        """
        print(f"Сейчас вы находитесь: {self.temp_dir}")
        if os.listdir(path=self.temp_dir):
            for entity_name in os.listdir(path=self.temp_dir):
                print(entity_name)
        else:
            print("В директории нет файлов!")

    def get_current(self):
        """
        Возвращает путь к текущей директории (где рогатка)
        :return: String
        """
        return self.temp_dir


    @staticmethod
    def __not_path(file_name):
        """
        Метод для проверки, что строка не путь
        :param file_name: String
        :return: boolean
        """
        if "/" not in file_name:
            return True
        else:
            return False

    def goto(self, new_dir):
        """
        Cмена директории (аналог cd)
        :param new_dir: String
        """
        if len(new_dir) == 6 and new_dir[4] == new_dir[5] == ".":
            if self.temp_dir != self.home_dir:
                temp = self.temp_dir[:self.temp_dir.rfind("/")]
                os.chdir(temp)
                self.temp_dir = temp
        elif len(new_dir) == 7 and new_dir[5]==new_dir[6] and new_dir[4] == " ":
            print("Воспользуйтесь командой goto.. для перехода выше")
        elif len(new_dir) > 6 and new_dir[4] == " ":

            name = new_dir.replace("goto ", "")
            try:
                temp = self.temp_dir + "/" + name
                os.chdir(temp)
                self.temp_dir = temp
            except Exception:
                print("Нет такой директории. Введите files для посмотра содержания текущей директории.")

    def create(self, command):
        """
        Создание директории
        :param command: String
        """
        try:
            name = command.replace("create ", "")
            os.mkdir(self.temp_dir + "/" + name)
            print("Папка успешно создана.")
        except Exception as e:
            print("Папки не существует или вы не ввели правильно команду..")

    def delete(self, command):
        """
        Удаление (папки или файла по названию)
        :param command: String
        """
        name = command.replace("delete ", "")
        try:
            shutil.rmtree(self.temp_dir + "/" + name)
            print("Удаление папки прошло успешно.")
        except Exception as e:
            try:
                os.remove(self.temp_dir + "/" + name)
                print("Удаление файла прошло успешно.")
            except Exception as e:
                print("Папки или файла не существует или вы не ввели правильно команду.")

    def make(self, command):
        """
        Создание пустого файла с конкретным названием
        :param command: String
        """
        try:
            name = command.replace("make ", "")
            if not name.startswith(" "):
                with open(self.temp_dir + "/" + name, "w"):
                    pass
                print("Файл успешно создан.")
            else:
                print("Недопустимое имя файла.")
        except Exception as e:
            print("Папки не существует или в названии присутствуют недопустимые символы.")

    def write(self, command):
        """
        Запись содержимого в файл
        :param command: String
        """
        try:
            name = command.replace("write ", "")
            text = name[name.find(" ") + 1:]
            name = name[:name.find(" ")]
            with open(self.temp_dir + "/" + name, "a+") as f:
                f.write("\n" + text)
            print("Данные записаны.")
        except Exception as e:
            print("Файла не существует.")

    def read(self, command):
        """
        Чтение содержимого файла
        :param command: String
        """
        try:
            name = command.replace("read ", "")
            with open(self.temp_dir + "/" + name, "r") as f:
                line = f.read()
                print(line)
        except Exception as e:
            print("Файла не существует или вы не ввели правильно команду..")

    def copy(self, command):
        """
        Копирование указаного файла в указанную директорию
        :param command: String
        """
        try:
            comm = command.replace("copy ", "")
            first_file = comm[:comm.find(" ")]
            comm = comm.replace(first_file + " ", "")
            second_file = comm
            if self.__not_path(first_file) and self.__not_path(second_file):
                if self.home_dir in first_file and self.home_dir in second_file:
                    shutil.copyfile(self.temp_dir + "/" + first_file, self.temp_dir + "/" + second_file)
            else:
                if first_file[0] == "/":
                    first_file = first_file.replace("/","")
                if second_file[0] == "/":
                    second_file = second_file.replace("/","")
                shutil.copyfile(self.home_dir+"/"+first_file, self.home_dir+"/"+second_file)
                print("Содержимое файла было успешно скопировано.")
        except Exception as e:
            print(e)
            print("Файла не существует или вы не ввели правильно команду.")
            print("Примечание: если в пути есть символы '/', то значит вы указываете абс. путь относительно корня менеджера")

    def move(self, command):
        """Перемещение указанного файла или директории в указанную директорию
        :param command: String
        """
        try:
            comm = command.replace("move ", "")
            first_file = comm[:comm.find(" ")]
            comm = comm.replace(first_file + " ", "")
            second_file = comm
            if self.__not_path(first_file):
                if self.__not_path(second_file):
                    shutil.move(self.temp_dir + "/" + first_file, self.temp_dir + "/" + second_file)
                else:
                    if second_file[0] == "/":
                        second_file = second_file.replace("/", "")
                    shutil.move(self.temp_dir + "/" + first_file, self.home_dir+"/"+second_file)
            else:
                if first_file[0] == "/":
                    first_file = first_file.replace("/", "")
                if self.__not_path(second_file):
                    shutil.move(self.home_dir + "/" + first_file, self.temp_dir + "/" + second_file)
                else:
                    if second_file[0] == "/":
                        second_file = second_file.replace("/", "")
                    shutil.copyfile(self.home_dir + "/" + first_file, self.home_dir + "/" + second_file)
        except shutil.Error:
            print("Данный файл итак находится в данной папке.")
        except Exception as e:
            print("Файла не существует или вы не ввели правильно команду.")
            print("Примечание: если в пути есть символы '/', то значит вы указываете абс. путь относителя корня менеджера")

    def rename(self, command):
        """
        Переименовывание указаного файла"
        :param command: String
        """
        try:
            comm = command.replace("rename ", "")
            first_file = comm[:comm.find(" ")]
            comm = comm.replace(first_file + " ", "")
            second_file = comm
            if self.__not_path(first_file) and self.__not_path(second_file):
                os.rename(self.temp_dir + "/" + first_file, self.temp_dir + "/" +second_file)
                print("Файл успешно переименован.")
            else:
                print("Файла не существует.")
        except Exception as e:
            print("Файла не существует или вы не ввели правильно команду.")



