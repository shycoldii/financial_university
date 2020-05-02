import table

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
        Game.set_checkers(color)
    @staticmethod
    def default_fields():
        """Доступные клетки для white/black"""
        white = []
        black = []
        for i in range(1, 9):
                if i % 2 == 1:
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
        white,black=Game.default_fields()
        for i in range(6):
          print(template)
          while True:
               while True:
                   position_1=input(f'Введи номер строки для {i+1}-ой шашки')
                   if position_1 in ['1','2','3','4','5','6','7','8']:
                       break
               while True:
                   position_2=input(f'Введи букву столбца для {i+1}-ой шашки')
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
          #тут будет гений рандома
        print('Начало игры')
        print(template)

    @staticmethod
    def generate_code(position_1,position_2):
            code=position_2+position_1
            return code


Game.start_menu()



