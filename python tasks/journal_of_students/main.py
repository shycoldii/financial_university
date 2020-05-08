try:
    students = []
    ok = ['25.02.20', '27.03.20', '29.04.20', '25.05.20', '13.06.20', '20.06.20']
    zapret = ['30.02.20', '31.02.20', '31.04.20']
    questions = ['Практика 1', 'Практика 2', 'Практика 3', 'Контрольная работа', 'Тестирование']
    questions1 = {}
    questions2 = {}
    questions1['Практика 1'] = ['25', '03', '20']
    questions1['Практика 2'] = ['27', '03', '20']
    questions1['Практика 3'] = ['29', '04', '20']
    questions2['Практика 1'] = ['25', '05', '20']
    questions2['Практика 2'] = ['13', '06', '20']
    questions2['Практика 3'] = ['20', '06', '20']


    class Diary:


        @staticmethod
        def student():
            print('Здравствуйте. Давайте заполним информацию о студентах.')
            while True:
                dates = []

                def pretty_form_python(name, subject, ex, balls, result):
                    print('-------------------------------------')
                    print(f'Имя студента: {name}')
                    print(f'     Предмет: {subject}')
                    print('\n')
                    print(f'Баллы за 1 практику: {balls[0]}')
                    print(f'Баллы за 2 практику: {balls[1]}')
                    print(f'Баллы за 3 практику: {balls[2]}')
                    print(f'Баллы за 1 контрольную работу: {balls[3]}')
                    print(f'Баллы за 1 тестирование: {balls[4]}')
                    print(f'Баллы за 4 практику: {balls[5]}')
                    print(f'Баллы за 5 практику: {balls[6]}')
                    print(f'Баллы за 6 практику: {balls[7]}')
                    print(f'Баллы за 2 контрольную работу: {balls[8]}')
                    print(f'Баллы за 2 тестирование: {balls[9]}')
                    print(f'Баллы за экзамен: {ex}')
                    print('\n')
                    print(f'Итоговый балл: {result}')
                    print('-------------------------------------')

                def pract(d1, d2, i, j):
                    def marks(date1, date2, q):
                        if date2[2] == q[2]:
                            if date2[1] == q[1]:
                                if date2[0] >= q[0]:
                                    if int(date2[0]) - int(q[0]) <= 7:
                                        return 4
                                    elif int(date2[0]) - int(q[0]) <= 14:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                            elif date2[1] > q[1]:
                                rr = int(date2[0]) + 31 - int(q[0])
                                if rr <= 7:
                                    return 4
                                elif rr <= 15:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 0

                    date1, date2 = [], []
                    if d1 != '-':

                        date1 = d1.split('.')
                        if len(date1) != 3:
                            raise ValueError
                        if int(date1[0]) < 1 or int(date1[0]) > 31:
                            raise ValueError

                        if int(date1[1]) < 1 or int(date1[1]) > 12:
                            raise ValueError
                    if d2 != '-':

                        date2 = d2.split('.')
                        if len(date2) != 3:
                            raise ValueError
                        if int(date2[1]) < 1 or int(date2[1]) > 12:
                            raise ValueError
                        if int(date2[0]) < 1 or int(date2[0]) > 31:
                            raise ValueError
                    if d1 in zapret:
                        print('Даты не существует.')
                        raise ValueError
                    if d2 in zapret:
                        print('Даты не существует.')
                        raise ValueError
                    if d2 == '-':
                        return 0
                    else:
                        if j == 0:
                            if date2 == [] or d2 == '-':
                                e = 0
                            if d1 == '-' and d2 == '-':
                                e = 0
                            if date1 == [] and date2 == []:
                                e = 0
                            if date2 != [] and d1 == '-':
                                e = 0
                            else:
                                q = questions1[i]
                                e = marks(date1, date2, q)
                                # функуция по подсчету даты


                        elif j == 1:
                            if date2 == [] or d2 == '-':
                                e = 0
                            if d1 == '-' and d2 == '-':
                                e = 0
                            if date1 == [] and date2 == []:
                                e = 0
                            if date2 != [] and d1 == '-':
                                e = 0
                            else:
                                q = questions2[i]
                                e = marks(date1, date2, q)
                        return e

                name = input('Введите фамилию и имя студента. Например: Alexandrova Dasha')
                subject = input('Введите предмет. Например: Python, Математика или Право')
                balls = []
                if subject == 'Python':
                    for j in range(2):
                        print(f'Выставим аттестацию {j + 1}')
                        for i in questions:

                            if i == 'Практика 1' or i == 'Практика 2' or i == 'Практика 3':
                                print('Если работа не сдана, напишите -.')
                                d1 = input(f'Введите дату выполнения  задания {i}. Например, 22.02.20')
                                d2 = input(f'Введите дату защиты  задания {i}. Например, 22.02.20')

                                e = pract(d1, d2, i, j)
                                balls.append(e)


                            elif i == 'Контрольная работа':
                                b = input('Введите количество баллов за контрольную работу(5 баллов). Например: 2.')
                                while int(b) > 5 or int(b) < 0:
                                    b = input('Введите количество баллов за контрольную работу(5 балла). Например: 3')
                                balls.append(b)
                            else:
                                b = input('Введите количество баллов за тестирование(3 балла). Например: 3')
                                while int(b) > 3 or int(b) < 0:
                                    b = input('Введите количество баллов за тестирование(3 балла). Например: 3')
                                balls.append(b)
                    result = 0
                    ex = int(input('Введите количество баллов за экзамен(60 баллов).'))
                    while int(ex) < 0 or int(ex) > 60:
                        ex = input("Введите баллы за экзамен. Всего 60 баллов. ")
                    for i in balls:
                        result += int(i)
                    result += ex
                    if result <= 100:

                        print('Проверьте данные и мы занесем их в таблицу.')
                        pretty_form_python(name, subject, ex, balls, result)
                        okey_go = input(
                            'Вас все устраивает? Если да, то введите +. Если нет, то аккаунт будет удален и вы сможете создать новую запись.')
                        if okey_go == '+':
                            if subject == 'Python':
                                f = open('Python.txt', 'a+')
                                f.write(str(name) + '|' + str(balls[0]) + "|" + str(balls[1]) + "|" + str(
                                    balls[2]) + "|" + str(balls[3]) + "|" + str(balls[4]) + "|" + str(
                                    balls[5]) + "|" + str(balls[6]) + "|" + str(balls[7]) + "|" + str(
                                    balls[8]) + "|" + str(balls[9]) + '|' + str(ex) + '||' + str(result))
                                f.write('\n')
                                f.close()
                    else:
                        print(
                            'Вероятно, произошла ошибка при подсчете баллов. Баллов оказалось больше 100. Пересоздайте студента.')
                elif subject == 'Математика':
                    result = 0
                    kr_1 = input("Введите баллы за контрольную 1. Всего 20 баллов. ")
                    while int(kr_1) < 0 or int(kr_1) > 20:
                        kr_1 = input("Введите баллы за контрольную 1. Всего 20 баллов. ")
                    kr_2 = input("Введите баллы за контрольную 2. Всего 20 баллов. ")
                    while int(kr_2) < 0 or int(kr_2) > 20:
                        kr_2 = input("Введите баллы за контрольную 2. Всего 20 баллов. ")
                    ex = input('Введите баллы за экзамен. Всего баллов 60.')
                    while int(ex) < 0 or int(ex) > 60:
                        ex = input("Введите баллы за экзамен. Всего 60 баллов. ")
                    result = result + int(ex) + int(kr_2) + int(kr_1)
                    if result <= 100:

                        print('Проверьте данные и мы занесем их в таблицу.')
                        print('-------------------------------------')
                        print(f'Имя студента: {name}')
                        print(f'     Предмет: {subject}')
                        print('\n')
                        print(f'Баллы за 1 контрольную работу: {kr_1}')
                        print(f'Баллы за 2 контрольную работу: {kr_2}')
                        print(f'Баллы за экзамен: {ex}')
                        print('\n')
                        print(f'Итоговый балл: {result}')
                        print('-------------------------------------')
                        okey_go = input(
                            'Вас все устраивает? Если да, то введите +. Если нет, то аккаунт будет удален и вы сможете создать новую запись.')
                        if okey_go == '+':
                            if subject == 'Математика':
                                f = open('Math.txt', 'a+')
                                f.write(
                                    str(name) + '|' + str(kr_1) + '|' + str(kr_2) + '|' + str(ex) + '||' + str(result))
                                f.write('\n')
                                f.close()
                    else:
                        print(
                            'Вероятно, произошла ошибка при подсчете баллов. Баллов оказалось больше 100. Пересоздайте студента.')
                elif subject == 'Право':
                    result = 0
                    kr_1 = input("Введите баллы за аттестацию 1. Всего 20 баллов. ")
                    while int(kr_1) < 0 or int(kr_1) > 20:
                        kr_1 = input("Введите баллы за аттестацию  1. Всего 20 баллов. ")
                    kr_2 = input("Введите баллы за аттестацию 2. Всего 20 баллов. ")
                    while int(kr_2) < 0 or int(kr_2) > 20:
                        kr_2 = input("Введите баллы за аттестацию 2. Всего 20 баллов. ")
                    ex = input('Введите баллы за экзамен. Всего баллов 60.')
                    while int(ex) < 0 or int(ex) > 60:
                        ex = input("Введите баллы за экзамен. Всего 60 баллов. ")
                    result = result + int(ex) + int(kr_2) + int(kr_1)
                    if result <= 100:

                        print('Проверьте данные и мы занесем их в таблицу.')
                        print('-------------------------------------')
                        print(f'Имя студента: {name}')
                        print(f'     Предмет: {subject}')
                        print('\n')
                        print(f'Баллы за 1 аттестацию: {kr_1}')
                        print(f'Баллы за 2 аттестацию: {kr_2}')
                        print(f'Баллы за экзамен: {ex}')
                        print('\n')
                        print(f'Итоговый балл: {result}')
                        print('-------------------------------------')
                        okey_go = input(
                            'Вас все устраивает? Если да, то введите +. Если нет, то аккаунт будет удален и вы сможете создать новую запись.')
                        if okey_go == '+':
                            if subject == 'Право':
                                f = open('Jurisprudence.txt', 'a+')
                                f.write(
                                    str(name) + '|' + str(kr_1) + '|' + str(kr_2) + '|' + str(ex) + '||' + str(result))
                                f.write('\n')
                                f.close()
                    else:
                        print(
                            'Вероятно, произошла ошибка при подсчете баллов. Баллов оказалось больше 100. Пересоздайте студента.')
                else:
                    print('Предмет не найден.')
                ask = input('Введите "да", если хотите завершить работу с заполнением студентов.')
                if ask.lower() == 'да':
                    return 1

    Diary.student()
except ValueError:
    print('Что-то не так.')