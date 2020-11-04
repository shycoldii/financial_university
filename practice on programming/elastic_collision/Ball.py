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

        def precitable_r(ob1, ob2, t):
            g=1000
            dt = 0.01
            #здесь t - это ob1.t0+t (потому что относительно отдельного шарика)
            t1 = t - ob1.t0 + dt
            t2 = t - ob2.t0 + dt

            # находим новые координаты
            coords1 = np.array([ob1.vx * t1 + ob1.x0, g * t1 * t1 / 2 + ob1.vy * t1 + ob1.y0])
            coords2 = np.array([ob2.vx * t2 + ob2.x0, g * t2 * t2 / 2 + ob2.vy * t2 + ob2.y0])
            return np.linalg.norm( coords1 - coords2)

        def elastic_collision(ob1, ob2, t):
            """
            :param ob1: объект первого шарика
            :param ob2: объект второго шарика
            :param t: время
            :return: vx,xy
            """
            g=1000
            # сколько времени прошло для каждого относительно одного
            t1 = t - ob1.t0
            t2 = t - ob2.t0
            #находим новые проекции скорости по y
            v1y = g * t1 + ob1.vy
            v2y = g * t2 + ob2.vy

            dx = ob2.coords[0] - ob1.coords[0]
            if dx == 0:
                phi = math.pi / 2
            else:
                phi = math.atan((ob2.coords[1] - ob1.coords[1]) / dx)

            def vector_angle(v):
                ba = np.array(v)
                dot = ba[0]
                det = ba[1]
                return math.atan2(det, dot)

            #находим углы между ними по двум проекциям
            theta1 = vector_angle([ob1.vx, v1y])
            theta2 = vector_angle([ob2.vx, v2y])

            #находим новые скорости
            v1 = math.sqrt(ob1.vx * ob1.vx + v1y * v1y)
            v2 = math.sqrt(ob2.vx * ob2.vx + v2y * v2y)
            #считаем новые проекции скроростей
            vx = (v1 * math.cos(theta1 - phi) * (ob1.m - ob2.m) + 2 * ob2.m * v2 * math.cos(theta2 - phi)) / (ob1.m + ob2.m)
            vx = vx * math.cos(phi) + v1 * math.sin(theta1 - phi) * math.cos(phi + math.pi / 2)
            vy = vx * math.sin(phi) + v1 * math.sin(theta1 - phi) * math.sin(phi + math.pi / 2)

            return vx, vy

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

        #====работа с другими шариками относительно первого, если они есть
        for i, j in zip(other, range(len(other))):
            r = np.linalg.norm(np.array(self.coords)-np.array(i.coords))
            if self.radius + i.radius >= r > precitable_r(self, i, t + self.t0):
                #случай столкновения
                v1x, v1y = elastic_collision(self, i, t + self.t0)
                v2x, v2y = elastic_collision(i, self, t + self.t0)
                #на основе новых проекциях считаем конечные скорости
                t1 = t + self.t0 - i.t0
                v1y = v1y - g * t
                v2y = v2y - g * t1
                self.x0 += t * (self.vx - v1x)
                i.x0 += (t + self.t0 - i.t0) * (i.vx - v2x)
                self.y0 += t * (self.vy - v1y)
                i.y0 += (t + self.t0 - i.t0) * (i.vy - v2y)
                self.vx = v1x
                self.vy = v1y
                i.vx = v2x
                i.vy = v2y

                if r < self.radius + i.radius:
                    r = self.radius + i.radius
                    if self.coords[1] < i.coords[1]:
                        ob1 = self
                        ob2 = i
                        t1 = t
                    else:
                        ob1 = i
                        ob2 = self
                    a = np.array(self.coords)
                    b = np.array(i.coords)
                    ab = a - b
                    if ab[1] > 0:
                        ab = - ab
                    theta = math.atan2(ab[1], ab[0])
                    if ob1.radius == ob2.radius and theta in [0, math.pi]:
                        if ob1.coords[0] > ob2.coords[0]:
                            theta = 0
                        else:
                            theta = math.pi
                    x = r * math.cos(theta) + ob2.coords[0]
                    if not ab[0]:
                        y = ob2.coords[1] - r
                    else:
                        y = ab[1] / ab[0] * x + ob2.coords[1] - ab[1] / ab[0] * ob2.coords[0]

                    ob1.y0 = y - g * t1 * t1 / 2 - ob1.vy * t1
                    ob1.x0 = x - ob1.vx * t1