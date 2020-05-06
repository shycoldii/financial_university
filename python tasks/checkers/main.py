import table
import random


class Game:
    def __init__(self):
        self.format_2 = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
        }
        self.good_lines_w = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
        self.good_lines_b = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']

    @staticmethod
    def start_menu():
        colors = {
            'Ч': 'черных',
            'Б': 'белых',
        }
        print('Привет, соискатель! Давай поиграем в шашки?')
        print('За кого будешь играть?')
        while True:
            print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
            color = input('Введи "Ч", если хочешь играть за черных \nВведи "Б", если хочешь играть за белых')
            color = color.upper()
            if color == 'Ч' or color == 'Б':
                break
        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print(f'С цветом определились! Теперь ты возглавляешь {colors[color]}.')
        print('Данная игра начинается с самого интересного - середины! Давай расставим твои 6 шашек.')
        print('Учти, что будет честнее, если до дамок останется как минимум 2 линии. Поэтому даже не пытайся...')
        Game.set_checkers(color)

    @staticmethod
    def default_fields():
        """Доступные клетки для white/black"""
        white = []
        black = []
        for i in range(1, 9):
            if i % 2 == 1:
                if i != 7:
                    white.append(f'b{i}')
                    white.append(f'd{i}')
                    white.append(f'f{i}')
                    white.append(f'h{i}')
                if i != 1:
                    black.append(f'b{i}')
                    black.append(f'd{i}')
                    black.append(f'f{i}')
                    black.append(f'h{i}')
            else:
                if i != 2:
                    black.append(f'a{i}')
                    black.append(f'c{i}')
                    black.append(f'e{i}')
                    black.append(f'g{i}')
                if i != 8:
                    white.append(f'a{i}')
                    white.append(f'c{i}')
                    white.append(f'e{i}')
                    white.append(f'g{i}')
        return white, black

    @staticmethod
    def set_checkers(color):
        format_template, template = table.Board().render()
        move = 0
        white, black = Game.default_fields()
        if color == 'Ч':
            status = 1
        else:
            status = 0
        for i in range(12):
            print(template)
            if (status == 0 and i % 2 == 0) or (status == 1 and i % 2 == 1):
                move += 1
                while True:
                    while True:
                        position_1 = input(f'Введи номер строки для {move}-ой шашки')
                        if position_1 in ['1', '2', '3', '4', '5', '6', '7', '8']:
                            break
                    while True:
                        position_2 = input(f'Введи букву столбца для {move}-ой шашки')
                        if position_2 in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                            break
                    code = Game.generate_code(position_1, position_2)
                    if color == 'Б':
                        if code in white:
                            station = table.Board().checking(format_template, position_1, position_2)
                            if station == True:
                                format_template, template = table.Board().render([position_1, position_2, color],
                                                                                 format_template)
                                break
                            else:
                                print('Ячейка занята. Перезапишите.')
                    else:
                        if code in black:
                            station = table.Board().checking(format_template, position_1, position_2)
                            if station == True:
                                format_template, template = table.Board().render([position_1, position_2, color],
                                                                                 format_template)
                                break
                            else:
                                print('Ячейка занята. Перезапишите.')
            if (status == 0 and i % 2 == 1) or (status == 1 and i % 2 == 0):
                while True:
                    # робот
                    if status == 0:
                        code = random.choice(black)
                    else:
                        code = random.choice(white)
                    position_1 = code[1]
                    position_2 = code[0]
                    good_field = table.Board().smart_bot(position_1, position_2, format_template)
                    if good_field == ['111']:
                        station = table.Board().checking(format_template, position_1, position_2)
                        if station == True:
                            if color == 'Ч':
                                format_template, template = table.Board().render([position_1, position_2, 'Б'],
                                                                                 format_template)
                            else:
                                format_template, template = table.Board().render([position_1, position_2, 'Ч'],
                                                                                 format_template)
                            break

        print('********************************************************')
        print('*********************НАЧАЛО ИГРЫ************************')
        print('********************************************************')

        Game().game_process(template, format_template, color)
        # здесь вызовем функцию с процессом игры

    @staticmethod
    def generate_code(position_1, position_2):
        code = position_2 + position_1
        return code

    def get_info_about_position(self, format_template, color):
        diagonals = []
        for i in range(len(format_template)):
            for j in range(len(format_template[i])):
                if format_template[i][j] == color:
                    our_check_1 = i + 1
                    our_check_2 = self.format_2[j]
                    diagonals = Game.can_to_move(color, our_check_1, our_check_2, format_template)
                    if diagonals != []:
                        return diagonals, our_check_1, our_check_2
        return diagonals, '', ''

    def game_process(self, template, format_template, color):
        kings = []
        move = 0  # счетчик кода
        while True:
            stop_code = 1
            code_not_ok = 0
            win_1, win_2 = 0, 0
            print(template)
            b, w, bw, king = table.Board.count_checkers(format_template)
            good_list_1, our_dictionary_1 = Game.prompt(format_template, 'Б')
            good_list_2, our_dictionary_2 = Game.prompt(format_template, 'Ч')
            if good_list_1 == [] and good_list_2 == []:
                diagonals_1, our_check_1, our_check_2 = Game().get_info_about_position(format_template, 'Б')
                diagonals_2, our_check_1, our_check_2 = Game().get_info_about_position(format_template, 'Ч')
                if diagonals_1 == [] and diagonals_2 == []:
                    code_not_ok = 1
                elif diagonals_1 == [] and diagonals_2 != []:
                    win_2 = 1
                elif diagonals_1 != [] and diagonals_2 == []:
                    win_1 = 1
            if bw == 0 or king > 0 or code_not_ok == 1 or win_2 == 1 or win_1 == 1 or w == 0 or b == 0:  # игра закончена
                colors = {'Б': 'БЕЛЫХ', 'Ч': 'ЧЕРНЫХ'}
                if king == 2:
                    color1 = 'Б'
                    print(f'********ПОБЕДИЛ ИГРОК, ИГРАЮЩИЙ ЗА {colors[color1]}********')
                if king == 1:
                    print(f'********ПОБЕДИЛ ИГРОК, ИГРАЮЩИЙ ЗА {colors[kings[0]]}********')
                elif win_1 == 1 or w == 0:
                    color_x = 'Б'
                    print(f'******************ПОБЕДИЛ ИГРОК, ИГРАЮЩИЙ ЗА {colors[color_x]}*******************')
                elif win_2 == 1 or b == 0:
                    color_x = 'Ч'
                    print(f'******************ПОБЕДИЛ ИГРОК, ИГРАЮЩИЙ ЗА {colors[color_x]}*******************')
                else:
                    print(f'********ПОБЕДИЛА ДРУЖБА********')
                break
            print(f'На поле сейчас: {w} белых и {b} черных шашек. Всего: {bw}')
            if color == 'Ч':
                status = 1  # если игрок играет за черных
            else:
                status = 0
            move += 1
            if (status == 1 and move % 2 == 0) or (status == 0 and move % 2 == 1):
                good_list, our_dictionary = Game.prompt(format_template, color)
                if good_list != []:
                    print('******************************ПОДСКАЗКА********************************')
                    print('Обычно, она доказывает, что вы имеете возможность сразиться!')
                    print('Поэтому даже не пытайтесь не сделать этого...')
                    print('Предупреждение: когда просят ввести "куда" - пишите клетку соперника')
                    print('******************************ПОДСКАЗКА********************************')
                    random_field = random.choice(good_list)
                    print(f'Вы можете сходить фишкой на следующей клетке: {random_field[0]}{random_field[1]}.')
                while True:
                    our_check_1 = input(f'Введите номер строки вашей шашки (которой хотите ходить)')
                    our_check_2 = input(f'Введите букву столбца вашей шашки (которой хотите ходить)')
                    if our_check_1 in ['1', '2', '3', '4', '5', '6', '7', '8'] and our_check_2 in ['a', 'b', 'c', 'd',
                                                                                                   'e',
                                                                                                   'f', 'g', 'h']:
                        check_it = table.Board().new_checking(format_template, our_check_1, our_check_2)
                        if (check_it == 'Black' and color == 'Ч') or (check_it == 'White' and color == 'Б'):
                            break
                        else:
                            print('Это не ваша шашка.')
                code_now = Game.generate_code(our_check_1, our_check_2)
                if good_list != [] and code_now not in good_list:
                    print('Пожалуйста, соблюдайте правила. Ваш оппонент намного честнее.')
                    move -= 1
                    stop_code = 0
                else:
                    while True:
                        position_1 = input(f'Введите номер строки для {move}-ого хода')
                        position_2 = input(f'Введите букву столбца для {move}-ого хода')
                        if position_1 in ['1', '2', '3', '4', '5', '6', '7', '8'] and position_2 in ['a', 'b', 'c', 'd',
                                                                                                     'e', 'f', 'g',
                                                                                                     'h']:
                            break
                    code = Game.generate_code(position_1, position_2)
                    chores_one, chores_two, chores = [], [], []
                    diagonals = Game.can_to_move(color, our_check_1, our_check_2, format_template)
                    if our_dictionary != {}:
                        chores = our_dictionary[code_now]
                        chores_one = chores[0:len(chores):2]
                        chores_two = chores[1:len(chores):2]
                    if (good_list != [] and code in chores_one):
                        hm = chores_one.index(code)
                        code_3 = chores_two[hm]
                        station = table.Board().new_checking(format_template, position_1, position_2)
                        if station != False:
                            format_template, template = table.Board().render([our_check_1, our_check_2, 'x'],
                                                                             format_template)
                        else:
                            print('Странная ошибка. Переходите.')
                            stop_code = 0
                            move -= 1
                        if (station == 'White' and status == 1) or (station == 'Black' and status == 0):
                            print('!!!ВЫ СОВЕРШИЛИ ПРОБИТИЕ!!!')

                        format_template, template = table.Board().render([position_1, position_2, 'x'],
                                                                         format_template)
                        if (code_3[1] == '1' and color == 'Ч') or (code_3[1] == '8' and color == 'Б'):
                            format_template, template = table.Board().render([code_3[1], code_3[0], 'Д'],
                                                                             format_template)
                            print(f'!!!{color}-ДАМКА ПОСТАВЛЕНА!!!')
                            kings.append(color)
                        else:
                            format_template, template = table.Board().render([code_3[1], code_3[0], color],
                                                                             format_template)
                    elif (good_list == [] and code in diagonals):
                        print(diagonals)
                        station = table.Board().new_checking(format_template, position_1, position_2)
                        if station != False:
                            format_template, template = table.Board().render([our_check_1, our_check_2, 'x'],
                                                                             format_template)
                        else:
                            move -= 1
                            print('Странная ошибка...Переходите.')
                            stop_code = 0
                        if (position_1 == '1' and color == 'Ч') or (position_1 == '8' and color == 'Б'):
                            format_template, template = table.Board().render([position_1, position_2, 'Д'],
                                                                             format_template)
                            print(f'!!!{color}-ДАМКА ПОСТАВЛЕНА!!!')
                            kings.append(color)
                        else:
                            format_template, template = table.Board().render([position_1, position_2, color],
                                                                             format_template)
                    else:
                        print('Ход недопустим. Возможно, стоит воспользоваться подсказкой. ')
                        stop_code = 0
                        move -= 1
            if (status == 1 and move % 2 == 1) or (status == 0 and move % 2 == 0):
                # тут уже робота
                if stop_code == 1:
                    if status == 1:
                        good_list, our_dictionary = Game.prompt(format_template, 'Б')
                    else:
                        good_list, our_dictionary = Game.prompt(format_template, 'Ч')
                    if good_list != []:
                        random_field = ''
                        random_one = ''
                        random_two = ''
                        for i in good_list:
                            chores = our_dictionary[i]
                            chores_one = chores[0:len(chores):2]
                            chores_two = chores[1:len(chores):2]
                            for j in chores_two:
                                if (status == 1 and j in self.good_lines_w) or (status == 0 and j in self.good_lines_b):
                                    hm = chores_two.index(j)
                                    random_one = chores_one[hm]
                                    random_two = j
                                    random_field = i
                                    break
                        if random_field == '':
                            random_field = random.choice(good_list)
                            chores = our_dictionary[random_field]
                            chores_one = chores[0:len(chores):2]
                            chores_two = chores[1:len(chores):2]
                            random_one = random.choice(chores_one)
                            hm = chores_one.index(random_one)
                            random_two = chores_two[hm]
                        station = table.Board().new_checking(format_template, random_field[1], random_field[0])
                        if station != False:
                            format_template, template = table.Board().render([random_field[1], random_field[0], 'x'],
                                                                             format_template)
                        format_template, template = table.Board().render([random_one[1], random_one[0], 'x'],
                                                                         format_template)
                        if status == 1:
                            color1 = 'Б'
                        else:
                            color1 = 'Ч'
                        if (random_two[1] == '1' and color1 == 'Ч') or (random_two[1] == '8' and color1 == 'Б'):
                            format_template, template = table.Board().render([random_two[1], random_two[0], 'Д'],
                                                                             format_template)
                            print(f'!!!{color1}-ДАМКА ПОСТАВЛЕНА!!!')
                            kings.append(color1)
                        else:
                            print(color1)
                            format_template, template = table.Board().render([random_two[1], random_two[0], color1],
                                                                             format_template)
                        print('Бот побил.')
                    else:
                        if status == 1:
                            color1 = 'Б'
                        else:
                            color1 = 'Ч'
                        diagonals, our_check_1, our_check_2 = Game().get_info_about_position(format_template, color1)
                        random_move = ''
                        if diagonals != []:
                            for i in diagonals:
                                if color1 == 'Ч':
                                    if i in self.good_lines_b:
                                        random_move = i
                                        break
                                else:
                                    if i in self.good_lines_w:
                                        random_move = i
                                        break
                            if random_move == '':
                                random_move = random.choice(diagonals)
                            station = table.Board().new_checking(format_template, our_check_1, our_check_2)
                            if station != False:
                                format_template, template = table.Board().render([our_check_1, our_check_2, 'x'],
                                                                                 format_template)
                            else:
                                move -= 1
                            if (random_move[1] == '1' and color1 == 'Ч') or (random_move[1] == '8' and color1 == 'Б'):
                                format_template, template = table.Board().render([random_move[1], random_move[0], 'Д'],
                                                                                 format_template)
                                print(f'!!!{color1}-ДАМКА ПОСТАВЛЕНА!!!')
                                kings.append(color1)
                            else:
                                format_template, template = table.Board().render(
                                    [random_move[1], random_move[0], color1],
                                    format_template)
                            print('Бот сходил.')

        print('Лог игры будет записан в этой папке. Хотите сделать рестарт?')
        ask_it = input('Введите +, если да. Иначе игра завершится. ')
        if ask_it == '+':
            # перезапуск
            Game.restart()

    @staticmethod
    def restart():
        Game.start_menu()

    @staticmethod
    def can_to_move(color, our_check_1, our_check_2, format_template):
        needs = []
        diagonals = Game.generate_diagonal(color, our_check_1, our_check_2)
        for i in diagonals[::-1]:
            station = table.Board().new_checking(format_template, i[1], i[0])
            if (station == 'White' and color == 'Б') or (station == 'Black' and color == 'Ч'):
                diagonals.remove(i)
            if station == 'White' and color == 'Ч':
                needs.append(i)
                diagonals.remove(i)
            elif station == 'Black' and color == 'Б':
                needs.append(i)
                diagonals.remove(i)
        if color == 'Ч':
            before = Game.generate_diagonal('Б', our_check_1, our_check_2)
        else:
            before = Game.generate_diagonal('Ч', our_check_1, our_check_2)
        for i in before:
            station = table.Board().new_checking(format_template, i[1], i[0])
            if station == 'White' and color == 'Ч':
                needs.append(i)
            elif station == 'Black' and color == 'Б':
                needs.append(i)
        return diagonals

    @staticmethod
    def prompt(format_template, color):
        format = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
        }
        format_2 = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }
        good_prompt = []
        our_dictionary = {}

        def inner(element, format_2, format, i, j):
            station1 = False
            next_step, next_next_step = '', ''
            try:
                if int(element[1]) - 1 > i and int(format_2[element[0]]) > j:  # пашет
                    next_step = element[0] + element[1]
                    next_next_step = format[format_2[element[0]] + 1] + str(int(element[1]) + 1)
                    station1 = table.Board().new_checking(format_template, int(element[1]) + 1,
                                                          format[format_2[element[0]] + 1])
                elif int(element[1]) - 1 > i and int(format_2[element[0]]) < j:  # пашет
                    next_step = element[0] + element[1]
                    next_next_step = format[format_2[element[0]] - 1] + str(int(element[1]) + 1)
                    station1 = table.Board().new_checking(format_template, int(element[1]) + 1,
                                                          format[format_2[element[0]] - 1])
                elif int(element[1]) - 1 < i and int(format_2[element[0]]) < j:  # пашет
                    station1 = table.Board().new_checking(format_template, int(element[1]) - 1,
                                                          format[format_2[element[0]] - 1])
                    next_step = element[0] + element[1]
                    next_next_step = format[format_2[element[0]] - 1] + str(int(element[1]) - 1)
                elif int(element[1]) - 1 < i and int(format_2[element[0]]) > j:
                    station1 = table.Board().new_checking(format_template, int(element[1]) - 1,
                                                          format[format_2[element[0]] + 1])

                    next_step = element[0] + element[1]
                    next_next_step = format[format_2[element[0]] + 1] + str(int(element[1]) - 1)
                if station1 == True:
                    good_prompt.append(f'{format[j]}{str(i + 1)}')
                    if f'{format[j]}{str(i + 1)}' in our_dictionary:
                        our_dictionary[f'{format[j]}{str(i + 1)}'] = our_dictionary[
                                                                         f'{format[j]}{str(i + 1)}'] + [
                                                                         next_step, next_next_step]
                    else:
                        our_dictionary[f'{format[j]}{str(i + 1)}'] = [next_step, next_next_step]
            except:
                station1 = False

        for i in range(len(format_template)):
            for j in range(len(format_template[i])):
                if color == 'Б':
                    if format_template[i][j] == 'Б':
                        list_diagonals = Game().diagonals(i, j)
                        for element in list_diagonals:
                            station = table.Board().new_checking(format_template, element[1], element[0])
                            if station == 'Black':
                                inner(element, format_2, format, i, j)
                else:
                    if format_template[i][j] == 'Ч':
                        list_diagonals = Game().diagonals(i, j)
                        for element in list_diagonals:
                            station = table.Board().new_checking(format_template, element[1], element[0])
                            if station == 'White':
                                inner(element, format_2, format, i, j)

        return good_prompt, our_dictionary

    def diagonals(self, i, j):
        format = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
        }

        my_list = []

        ok_1 = i - 1
        ok_2 = i + 1
        ok_3 = j - 1
        ok_4 = j + 1

        if ok_1 < 0:
            if ok_4 > 7:
                my_list.append(f'{str(format[j - 1])}{str(i + 2)}')
            else:
                my_list.append(f'{str(format[j - 1])}{str(i + 2)}')
                my_list.append(f'{str(format[j + 1])}{str(i + 2)}')
        elif ok_3 < 0:
            if ok_2 > 7:
                my_list.append(f'{str(format[j + 1])}{str(i)}')
            else:
                my_list.append(f'{str(format[j + 1])}{str(i + 2)}')
                my_list.append(f'{str(format[j + 1])}{str(i)}')
        elif ok_2 > 7:
            my_list.append(f'{str(format[j - 1])}{str(i)}')
            my_list.append(f'{str(format[j + 1])}{str(i)}')
        elif ok_4 > 7:
            my_list.append(f'{str(format[j - 1])}{str(i)}')
            my_list.append(f'{str(format[j - 1])}{str(i + 2)}')
        else:
            my_list.append(f'{str(format[j - 1])}{str(i)}')
            my_list.append(f'{str(format[j + 1])}{str(i + 2)}')
            my_list.append(f'{str(format[j - 1])}{str(i + 2)}')
            my_list.append(f'{str(format[j + 1])}{str(i)}')
        return my_list

    @staticmethod
    def generate_diagonal(color, our_check_1, our_check_2):
        nums = []
        format = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }
        if color == 'Ч':
            number = int(our_check_1) - 1
        else:
            number = int(our_check_1) + 1
        if number % 2 == 0:
            good = [f'a{number}', f'c{number}', f'e{number}', f'g{number}']
        else:
            good = [f'b{number}', f'd{number}', f'f{number}', f'h{number}']
        nums.append(format[our_check_2] + 1)
        nums.append(format[our_check_2] - 1)
        if nums[0] == 9:
            nums.remove(nums[0])
        elif nums[1] == -1:
            nums.remove(nums[1])
        letters = []
        for key, item in format.items():
            if item in nums:
                letters.append(key + str(number))
        for i in good[::-1]:
            if i not in letters:
                good.remove(i)
        return good


Game.start_menu()
