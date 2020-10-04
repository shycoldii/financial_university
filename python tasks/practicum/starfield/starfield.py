import pygame
from random import uniform, randint
import numpy


(width, height) = (1024, 1024)


class star:
    (x,y,z,sx,sy) = (0.0,0.0,0.0,0,0)

    def __init__(self):
        self.reset()

    def reset(self):
        """
        изменение значения звезд относительно позиции мышки
        """
        mouse =  pygame.mouse.get_pos()
        if 490 <= mouse[0] <= 570 and 490 <=mouse[1] <= 570:
            self.x = uniform(-0.5, 0.5)
            self.y = uniform(-0.5, 0.5)
        else:
            if 0 <mouse[0] <= 512 and 0 <mouse[1]<=512:
                #print('левый верхний край')
                self.x = uniform(-mouse[1] / 5000,0)
                self.y = uniform(-mouse[0]/5000,0)
                #self.x = -mouse[1] / 1000
                #self.y = -mouse[0]/1000
                #self.y = uniform(self.y-0.005,self.y+0.005)
                #self.x = uniform(self.x - 0.005, self.x + 0.005)
            if mouse[0] >= 512 and mouse[0] <= 1024 and 0 <= mouse[1]<=512:
                #print('правый верхний край')
                self.x = uniform(0,mouse[1] / 5000)
                self.y = uniform(-mouse[0] / 5000,0)
            if 0<=mouse[0] <= 512 and mouse[1] >= 512 and  mouse[1]<=1024:
                #print('нижний левый край')
                self.x = uniform(-mouse[1] / 5000,0)
                self.y = uniform(0,mouse[0] / 5000)
            if mouse[0] >= 512 and mouse[1] >= 512 and mouse[0]<=1024 and mouse[1]<=1024:
                if 900<=mouse[0] <=1024 and 512<=mouse[1]<=700:
                    self.x = uniform(0, 0.4)
                    self.y = uniform(0, 0.1)
                else:
                #print('нижний правый край')
                    self.x = uniform(0,mouse[1] / 5000)
                    self.y = uniform(0, mouse[0] / 5000)
            else:
                pass
        self.z = uniform(0.5,1)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.max_size = randint(10,100)

    def update(self, speed):
        """
        движение звезд и при надобности их генерация
        :param speed: скорость
        """
        textsurface = myfont.render(f'Speed={round(speed,2)}', False,(255,255,255))
        screen.blit(textsurface, (0, 0))
        textsurface2 = myfont.render(f'Press Q to exit', False, (255, 255, 255))
        screen.blit(textsurface2, (800, 0))

        self.z -= speed/50
        self.sx = self.x / self.z
        self.sy = self.y / self.z
        if self.sx ==0 or self.sy == 0 or abs(self.sx) > 1 or abs(self.sy) > 1 or self.z < 0.01:
            self.reset()

    def show(self, screen):
        """показ звездного поля"""
        screen_x = int(numpy.interp(self.sx, [-1,1], [0, screen.get_width()]))
        screen_y = int(numpy.interp(self.sy, [-1,1], [0, screen.get_height()]))
        radius = int(numpy.interp(self.z, [0.0001, 1.0], [self.max_size, 0]))

        bright = numpy.interp(self.z,[0,1], [1.0,0.0])
        screen_color = tuple(map(lambda x: int(x * bright), self.color))
        pygame.draw.ellipse(screen,screen_color,pygame.Rect(screen_x, screen_y, radius,radius))


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("starfield by Dasha Alexandrova")
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
done = False

stars = []
for i in range(100): #создание звезд
    stars.append(star())

speed=0.005
print("Практика Александровой Дарьи")
print("----------------------------")
print("Используйте клавиши <вверх> и <вниз> для регуляции скорости")
print("Для выхода из игры нажмите q")
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            done = True
        if event.type ==pygame.KEYDOWN: #реакция на клавиатуру
            if event.key == pygame.K_UP:
                speed += 0.05
            elif event.key == pygame.K_DOWN:
                speed -= 0.05
            if speed <= 0:
                speed = 0

    screen.fill((0, 0, 0))
    stars.sort(key=lambda x: -x.z)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for s in stars:
        s.update(speed)
        s.show(screen)

    pygame.display.flip()