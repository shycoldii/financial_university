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

    @staticmethod
    def generate_code(position_1,position_2):
            code=position_2+position_1
            return code



Game.start_menu()



