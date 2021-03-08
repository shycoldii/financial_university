import configparser
import manager.file_manager


if __name__ == "__main__":
    #Инициализируем информацию из config.ini:
    config = configparser.ConfigParser()
    config.read('config.ini',encoding="utf-8")
    manager = manager.file_manager.FileManager(config["settings"]["WORKING_DIRECTORY"])
    if  not manager.is_exist():
          print("Невозможно начать работу с данной директорией.")
    else:
        print("=================================================================================")
        print(f"Добро пожаловать в файловый менеджер! Корень вашего проекта: {manager.home_dir}")
        print("Для знакомства с командами используйте команду help.")
        print("=================================================================================")
        while True:
            try:
                value = input("$" + manager.get_current()[manager.get_current().rfind("/") + 1:] + ">")
                if value.startswith("create "):
                    manager.create(value)
                elif value.startswith("delete "):
                    manager.delete(value)
                elif value.startswith("goto"):
                    manager.goto(value)
                elif value.startswith("make "):
                    manager.make(value)
                elif value.startswith("write "):
                    manager.write(value)
                elif value.startswith("read "):
                    manager.read(value)
                elif value.startswith("copy "):
                    manager.copy(value)
                elif value.startswith("move "):
                    manager.move(value)
                elif value.startswith("rename "):
                    manager.rename(value)
                elif value == "info":
                    manager.info()
                elif value == "help":
                    manager.help()
                else:
                    print("Команда не распознана.\nСписок доступных команд:")
                    manager.help()
            except KeyboardInterrupt as e:
                break
