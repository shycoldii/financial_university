class Board:

    def __init__(self):
        self.f1 = 'x'
        self.f2 = ' '
        self.f3 = 'Д'
        self.format = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }
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

    def checking(self, format_template, position_1, position_2):
        """обычное изучение позиции (проверка на крестик)"""
        if format_template[int(position_1) - 1][self.format[position_2]] == self.f1:
            return True
        else:
            return False

    def new_checking(self, format_template, position_1, position_2):
        """углубленное изучение позиции"""
        try:
            if format_template[int(position_1) - 1][self.format[position_2]] == self.f1:
                return True
            if format_template[int(position_1) - 1][self.format[position_2]] == 'Ч':
                return 'Black'
            if format_template[int(position_1) - 1][self.format[position_2]] == 'Б':
                return 'White'
            else:
                return False
        except:
            return False

    def smart_bot(self, position_1, position_2, format_template):
        """логика бота"""
        real_list, nums, special_nums, letter = [], [], [], []
        if position_1 != '8' and position_1 != '1' and position_2 != 'a' and position_2 != 'h':
            special_nums.append(self.format[position_2] - 1)
            special_nums.append(self.format[position_2] + 1)
            nums.append(int(position_1) + 1)
            nums.append(int(position_1) - 1)
            for key, item in self.format.items():
                if item == special_nums[0] or item == special_nums[1]:
                    letter.append(key)
            real_list.append(f'{letter[0]}{nums[0]}')
            real_list.append(f'{letter[0]}{nums[1]}')
            real_list.append(f'{letter[1]}{nums[0]}')
            real_list.append(f'{letter[1]}{nums[1]}')
            for i in real_list[::-1]:
                station = Board().checking(format_template, i[1], i[0])
                if station == False:
                    real_list.remove(i)
            if len(real_list) != 4:
                return ['000']
            else:
                return ['111']
        else:
            return ['111']

    @staticmethod
    def count_checkers(format_template):
        """считает количество шашек на данный момент"""
        black, white, count, king = 0, 0, 0, 0
        for i in format_template:
            black += i.count('Ч')
            white += i.count('Б')
            king += i.count('Д')
        count = black + white
        return black, white, count, king

    def render(self, stream=None, format_template=None):  # stream = (№строки, №столбца, фигура)
        """Меняет состояние доски после каждого вызова"""
        if format_template == None:
            format_template = [
                [self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1],
                [self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2],
                [self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1],
                [self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2],
                [self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1],
                [self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2],
                [self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1],
                [self.f1, self.f2, self.f1, self.f2, self.f1, self.f2, self.f1, self.f2],
            ]
        separator_1 = '  |-----------------------------------------------|\n'
        separator_2 = '  |-----+-----+-----+-----+-----+-----+-----+-----|\n'
        header = '  |  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |\n'
        template = header + separator_1
        if stream != None:
            format_template[int(stream[0]) - 1][self.format[stream[1]]] = stream[2]
        for i in range(len(format_template)):
            template += f'{i + 1} |  {format_template[i][0]}  |  {format_template[i][1]}  |  {format_template[i][2]} ' \
                        f' |  {format_template[i][3]}  |  {format_template[i][4]}  |  {format_template[i][5]}  ' \
                        f'|  {format_template[i][6]}  |  {format_template[i][7]}  | {i + 1}\n'
            template += separator_2
        template = template[:-52] + separator_1 + header
        return format_template, template
