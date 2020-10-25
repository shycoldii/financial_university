p=0 #счетчик игрока, отвечающий за четность и нечетность


def drawing(list): #функция рисует процесс игры


    print('     '.join(list[0]))
    print('     '.join(list[1]))
    print('     '.join(list[2]))


list = [ ['*','*','*'],
         ['*','*','*'],
         ['*','*','*']] #поле
player=['Игрок 1','Игрок 2'] #список, хранящий название игроков
p_znak=['X','O'] #список, преобразующий числа в символы крестиков и ноликов
drawing(list)
print('Это игра "Крестики-нолики". Собери нужную комбинацию и обыграй соперника!')
while True:
    r=0 #счетчик ничьи
    for i in range(3):
        for j in range(3):
            if list[i-1][j-1]!='*':
                r+=1
    if r==9: #если не осталось клеток-то ничья
        break
    #Ввод данных пользователем, где x y -координаты строки и столбца
    print(str(player[p%2])+',' +'ходи')
    x=input('Введите строку'+':'+' ')
    y=input('Введите столбец'+':'+' ')
    if x.isdigit()==False or y.isdigit()==False: #проверка вводимого
        print('Вы уверены, что ввели  целое число?')
        continue
    x=int(x)
    y=int(y)
    if x<1 or x>3 or y<1 or y>3: #проверка выхода за поле
        print('Вы ввели недопустимое число для поля')
        continue

    #проверка на условия вводимого, если человек красит уже закрашенное
    if list[x-1][y-1]=='X' or list[x-1][y-1]=='O':
                 print('Клетка уже закрашена. Попробуйте другую')
                 continue


    else:
        list[x-1][y-1]=p_znak[p%2]

    p+=1
    #комбинации для окончания игры
    if list[0][0]!='*'   and list[0][0]==list[1][1]==list[2][2]:
            break
    if list[0][2]!='*'   and list[0][2]==list[1][1]==list[2][0]:
            break
    if list[0][0]!='*' and list[0][0]==list[0][1]==list[0][2]:
        break
    if list[1][0]!='*' and list[1][0]==list[1][1]==list[1][2]:
        break
    if list[2][0]!='*' and list[2][1]==list[2][0]==list[2][2]:
        break
    if list[0][0]!='*' and list[0][0]==list[1][0]==list[2][0]:
        break
    if list[0][1] != '*' and list[0][1] == list[1][1] == list[2][1]:
        break
    if list[0][2] != '*' and list[0][2] == list[1][2] == list[2][2]:
        break
    else:
        drawing(list)

if r%9==0 and r!=0: #случай ничьи
    print('Игра окончена. Ничья!')
else:
   print('     '.join(list[0]))
   print('     '.join(list[1]))
   print('     '.join(list[2]))
   print('Игра окончена. Победил' +' ' +player[(p-1)%2])




















