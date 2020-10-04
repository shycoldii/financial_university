import pygame
from random import uniform, randint
import numpy


(width, height) = (1024, 1024)


class star:
    (x,y,z,sx,sy) = (0.0,0.0,0.0,0,0)

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = uniform(-0.5,0.5)
        self.y = uniform(-0.5,0.5)
        self.z = uniform(0.9,1.0)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.max_size = randint(10,50)

    def update(self, speed):

        self.z -= speed/50

        self.sx = self.x / self.z
        self.sy = self.y / self.z

        if self.sx ==0 or self.sy == 0 or abs(self.sx) > 1 or abs(self.sy) > 1 or self.z < 0.01:
            self.reset()

    def show(self, screen):
        screen_x = int(numpy.interp(self.sx, [-1,1], [0, screen.get_width()]))
        screen_y = int(numpy.interp(self.sy, [-1,1], [0, screen.get_height()]))
        radius = int(numpy.interp(self.z, [0.0001, 1.0], [self.max_size, 0]))

        bright = numpy.interp(self.z,[0,1], [1.0,0.0])
        screen_color = tuple(map(lambda x: int(x * bright), self.color))

        pygame.draw.ellipse(screen,screen_color,pygame.Rect(screen_x, screen_y, radius,radius))


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("starfield by Dasha Alexandrova")

done = False
speed=0.1
stars = []
for i in range(200):
    stars.append(star())
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
print("Практика Александровой Дарьи")
print("----------------------------")
print("Используйте клавиши <вверх> и <вниз> для регуляции скорости")
print("Для выхода из игры нажмите q")
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                done = True
            if event.type == pygame.KEYDOWN:
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
        textsurface = myfont.render(f'Speed={round(speed, 2)}', False, (255, 255, 255))
        textsurface2 = myfont.render(f'Press Q to exit', False, (255, 255, 255))
        screen.blit(textsurface2, (800, 0))
        screen.blit(textsurface, (0, 0))
        s.update(speed)
        s.show(screen)

    pygame.display.flip()