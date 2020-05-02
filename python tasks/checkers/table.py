class Board:

    def __init__(self):
        self.f1='x'
        self.f2 = ' '
        self.f3 = 'Д'


    def render(self,stream):  # stream = (№строки, №столбца, фигура)
        """Меняет состояние доски после каждого вызова"""
        format_template=[
            [self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1],
            [self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2],
            [self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1],
            [self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2],
            [self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1],
            [self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2],
            [self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1],
            [self.f1,self.f2,self.f1,self.f2,self.f1,self.f2,self.f1,self.f2],
        ]
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

        separator_1 = '  |-----------------------------------------------|\n'
        separator_2 = '  |-----+-----+-----+-----+-----+-----+-----+-----|\n'
        header = '  |  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |\n'
        template = header + separator_1
        format_template[stream[0]-1][format[stream[1]]] = stream[2]
        for i in range(len(format_template)):
            template += f'{i+1} |  {format_template[i][0]}  |  {format_template[i][1]}  |  {format_template[i][2]} ' \
                        f' |  {format_template[i][3]}  |  {format_template[i][4]}  |  {format_template[i][5]}  ' \
                        f'|  {format_template[i][6]}  |  {format_template[i][7]}  | {i+1}\n'
            template += separator_2
        template = template[:-52] + separator_1 + header
        return template

    def display(self):
        print(self.render([1, 'f', 'Б']))


a = Board()
a.display()
