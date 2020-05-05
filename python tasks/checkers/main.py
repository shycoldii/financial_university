import table
import random

class Game:
    def __init__(self):
        pass

    @staticmethod
    def start_menu():
        colors={
            'Ч':'черных',
            'Б': 'белых',
        }
        print('Привет, соискатель! Давай поиграем в шашки?')
        print('За кого будешь играть?')
        while True:
           print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
           color=input('Введи "Ч", если хочешь играть за черных \nВведи "Б", если хочешь играть за белых')
           color=color.upper()
           if color=='Ч' or color=='Б':
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
                    if i!=7:
                        white.append(f'b{i}')
                        white.append(f'd{i}')
                        white.append(f'f{i}')
                        white.append(f'h{i}')
                    if i!=1:
                        black.append(f'b{i}')
                        black.append(f'd{i}')
                        black.append(f'f{i}')
                        black.append(f'h{i}')
                else:
                    if i!=2:
                        black.append(f'a{i}')
                        black.append(f'c{i}')
                        black.append(f'e{i}')
                        black.append(f'g{i}')
                    if i!=8:
                        white.append(f'a{i}')
                        white.append(f'c{i}')
                        white.append(f'e{i}')
                        white.append(f'g{i}')
        return white,black

    @staticmethod
    def set_checkers(color):
        format_template,template=table.Board().render()
        move=0
        white,black=Game.default_fields()
        if color == 'Ч':
              status=1
        else:
            status=0
        for i in range(12):
          print(template)
          if (status==0 and i%2==0) or (status==1 and i%2==1):
              move+=1
              while True:
                   while True:
                       position_1=input(f'Введи номер строки для {move}-ой шашки')
                       if position_1 in ['1','2','3','4','5','6','7','8']:
                           break
                   while True:
                       position_2=input(f'Введи букву столбца для {move}-ой шашки')
                       if position_2 in ['a','b','c','d','e','f','g','h']:
                           break
                   code=Game.generate_code(position_1,position_2)
                   if color=='Б':
                       if code in white:
                            station=table.Board().checking(format_template,position_1,position_2)
                            if station==True:
                                 format_template, template = table.Board().render([position_1, position_2, color],format_template)
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
                  #робот
                  if status==0:
                      code=random.choice(black)
                  else:
                      code=random.choice(white)
                  position_1=code[1]
                  position_2=code[0]
                  good_field = table.Board().smart_bot(position_1, position_2,format_template)
                  if good_field == ['111']:
                      station = table.Board().checking(format_template, position_1, position_2)
                      if station == True:
                          if color=='Ч':
                              format_template, template = table.Board().render([position_1, position_2, 'Б'], format_template)
                          else:
                              format_template, template = table.Board().render([position_1, position_2, 'Ч'], format_template)
                          break

        print('********************************************************')
        print('*********************НАЧАЛО ИГРЫ************************')
        print('********************************************************')
        print(template)
        Game().game_process(template,format_template,color)
        #здесь вызовем функцию с процессом игры

    @staticmethod
    def generate_code(position_1,position_2):
            code=position_2+position_1
            return code
    def game_process(self,template,format_template,color):
        move = 0 #счетчик кода
        while True:
            print(template)
            if color=='Ч':
                status=1 #если игрок играет за черных
            else:
                status=0
            move+=1
            #здесь реализовать подсказку
            while True:
                our_check_1=input(f'Введите номер строки вашей шашки (которой хотите ходить)')
                our_check_2 = input(f'Введите букву столбца вашей шашки (которой хотите ходить)')
                if our_check_1 in ['1', '2', '3', '4', '5', '6', '7', '8'] and our_check_2 in ['a','b','c','d','e','f','g','h']:
                    break
            good_list, needs = Game().can_to_move(color, our_check_1, our_check_2, format_template)
            if needs != []:
                print('***ПОДСКАЗКА***')
                print('У вас есть возможность побить шашку соперника.')
                print(f'Рекомендуемый ход: {random.choice(needs)}')
            while True:
                position_1=input(f'Введите номер строки для {move}-ого хода')
                position_2=input(f'Введите букву столбца для {move}-ого хода')
                if position_1 in ['1', '2', '3', '4', '5', '6', '7', '8'] and position_2 in ['a','b','c','d','e','f','g','h']:
                    break
            code=Game.generate_code(position_1,position_2)
            if (needs != [] and code in needs) or (needs == [] and code in good_list):
                        station = table.Board().new_checking(format_template, position_1, position_2)
                        if station != False:
                            format_template, template = table.Board().render([our_check_1, our_check_2, 'x'],
                                                                             format_template)
                        if (station == 'White' and status == 1) or (station == 'Black' and status == 0):
                                print('!!!ВЫ СОВЕРШИЛИ ПРОБИТИЕ!!!')
                        if position_1 == '1':
                                format_template, template = table.Board().render([position_1, position_2, 'Д'],
                                                                                 format_template)
                                print(f'!!!{color}-ДАМКА ПОСТАВЛЕНА!!!')
                        else:
                                format_template, template = table.Board().render([position_1, position_2, color],
                                                                                 format_template)
            else:
                print('Ход недопустим. Возможно, стоит воспользоваться подсказкой. ')
                move -= 1
            #тут уже робота
        # тут выходим из игры и записываем в файл
    def can_to_move(self,color,our_check_1,our_check_2,format_template):
        needs=[]
        diagonals = Game().generate_diagonal(color, our_check_1, our_check_2)
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
            before = Game().generate_diagonal('Б', our_check_1, our_check_2)
        else:
            before = Game().generate_diagonal('Ч', our_check_1, our_check_2)
        for i in before:
            station = table.Board().new_checking(format_template, i[1], i[0])
            if station == 'White' and color == 'Ч':
                needs.append(i)
            elif station == 'Black' and color == 'Б':
                needs.append(i)
        return diagonals,needs
    def prompt(self,format_template,color):
        for i in range(len(format_template)):
            for j in range(format_template[i]):
                if i

    def generate_diagonal(self,color,our_check_1,our_check_2):
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
        for key,item in format.items():
            if item in nums:
                  letters.append(key+str(number))
        for i in good[::-1]:
            if i not in letters:
                good.remove(i)
        return good
Game.start_menu()



