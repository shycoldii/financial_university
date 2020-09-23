import math
from tkinter import *

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs)) #помогает нам на основе градусов давать синусы и косинусы
#при 180 вернет -1 для косинуса

def main():
   root = Tk()
   canvas = Canvas(root, width=600, height=600) #создает окно 600 на 600
   canvas.pack()
   creating_oval(canvas,root)
   motion(canvas,root)
def creating_oval(canvas,root):
    """
    :param canvas: объект canvas
    :param root: объект root
    :return: Фиолетовый круг нужного размера
    """
    color = '#bf95bf'
    x0 = 100
    y0 = 100
    d = 400
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=color)

def bounds(x,y,r):
    """Для окружности"""
    return (x + r*cos(0),   y + r*sin(270),
            x + r*cos(180), y + r*sin(90))
def motion(canvas,root):
    point = canvas.create_oval(bounds(300+200,300,10),fill="black",width=0) #поставили точку на окружности
    orbital_radius = math.hypot(300 - 500, 300 - 300)
    path = create_path(300,300,orbital_radius,10) #первые параметры отвечают за направление движения
    next(path)
    root.after(100,updating,canvas,point,500,300,path)
    root.mainloop()
def create_path(x,y,r,delta,start=0):
    """Генерирует координаты пути"""
    ang = start % 360 #координата на окружности от 0 до 360
    while True:
        yield x + r*cos(ang), y + r*sin(ang)
        ang = (ang+delta) % 360
def updating(canvas,id,x,y,path_iter):
    """Итерация и новые позиции"""
    x, y = next(path_iter)
    x0, y0, x1, y1 = canvas.coords(id)
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2
    dx, dy = x - oldx,y - oldy  # amount of movement
    canvas.move(id, dx, dy)
    canvas.after(100, updating, canvas, id, x,y,path_iter) #первый параметр отвечает за скорость
if __name__ =="__main__":
    main()
