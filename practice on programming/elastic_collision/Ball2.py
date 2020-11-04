import math
import random
import numpy as np
from pygame import gfxdraw
import Const

class ball:
    def __init__(self, x, y, vx, vy, t0,screen):
        """
        Класс, отвечающий за объект "Шарик"
        :param x: координата x
        :param y: координата y
        :param vx: проекция вектора скорости по x
        :param vy: проекция вектора скорости по x
        :param t0: начальное время движения
        :param screen: параметр экрана для обновления состояния
        """
        self.x0 = x
        self.y0 = y
        self.coords = [x, y]
        self.vx = vx
        self.vy = vy
        self.t0 = t0
        self.p = 1000 #плотность шариков
        self.screen = screen
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.m = (4/3)*math.pi*math.pow(self.radius,3)*self.p

    def draw(self):
        """
        Рисует шарик по координатам
        :return: параметр обновленного экрана
        """
        gfxdraw.aacircle(self.screen, int(self.coords[0]), int(self.coords[1]), self.radius, self.color)
        gfxdraw.filled_circle(self.screen, int(self.coords[0]), int(self.coords[1]), self.radius, self.color)
        return self.screen

    def update(self, t, other):

        g=1000
        height = Const.const.getparam()[0]
        width = Const.const.getparam()[1]
        t = t - self.t0 #разницу  стартового с текущим временем


        if self.coords[1] >= height - self.radius and 40 <= g * t + self.vy:
            #случай пола(скорость там положительна), когда скорость в полете превышает "условную допустимую 40"
            v2 = - (g * t + self.vy) * 0.5 #уменьшаем значение -0,5gt-0,5self.vy-gt=-1,5gt-0,5self.vu
            self.vy = v2 - g * t
            self.y0 = height - self.radius - g * t * t / 2 - self.vy * t
        elif self.coords[1] >= height - self.radius and -30 <= g * t + self.vy < 30:
            # случай пола, когда скорость в полете находится между "условной допустимой 40", то сделаем равной -gt
            self.vy = - g * t
            self.y0 = height - self.radius - g * t * t / 2 - self.vy * t
        #===обновляем координаты относительно нового времени
        self.coords[0] = self.vx * t + self.x0
        self.coords[1] = g * t * t / 2 + self.vy * t + self.y0

        if self.coords[0] > width - self.radius and self.vx > 0 or (self.coords[0] < self.radius and self.vx < 0):
            #случай стенок левых и правых
            self.x0 += 2 * self.vx * t
            self.vx *= -1

