import pygame
import math
from pygame import gfxdraw
import random
import numpy as np
import time


class ball:
    def __init__(self, x, y, vx, vy, t0):
        self.x0 = x
        self.y0 = y
        self.vx = vx
        self.vy = vy
        self.t0 = t0
        self.coords = [x, y]
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.mass = self.radius * self.radius / 10

    def update(self, t, other):
        g=1000
        def future_r(ob1, ob2, t):
            dt = 0.01
            t1 = t - ob1.t0 + dt
            t2 = t - ob2.t0 + dt
            coords1 = [ob1.vx * t1 + ob1.x0, g * t1 * t1 / 2 + ob1.vy * t1 + ob1.y0]
            coords2 = [ob2.vx * t2 + ob2.x0, g * t2 * t2 / 2 + ob2.vy * t2 + ob2.y0]
            coords1 = np.array(coords1)
            coords2 = np.array(coords2)
            vec = coords1 - coords2
            return np.linalg.norm(vec)


        t = t - self.t0
        if self.coords[1] >= height - self.radius and 30 <= g * t + self.vy:
            v2 = - (g * t + self.vy) * 0.7
            vy = v2 - g * t
            self.y0 += t * (self.vy - vy)
            self.vy = vy
            self.y0 = height - self.radius - g * t * t / 2 - self.vy * t
        elif self.coords[1] >= height - self.radius and -30 <= g * t + self.vy < 30:
            v2 = 0
            vy = v2 - g * t
            self.y0 += t * (self.vy - vy)
            self.vy = vy
            self.y0 = height - self.radius - g * t * t / 2 - self.vy * t
        self.coords[0] = self.vx * t + self.x0
        self.coords[1] = g * t * t / 2 + self.vy * t + self.y0
        if self.coords[0] > width - self.radius and self.vx > 0 or (self.coords[0] < self.radius and self.vx < 0):
            self.x0 += 2 * self.vx * t
            self.vx *= -1
        a = np.array(self.coords)
        for i, j in zip(other, range(len(other))):
            b = np.array(i.coords)
            ba = a - b
            r = np.linalg.norm(ba)
            if self.radius + i.radius >= r > future_r(self, i, t + self.t0):
                v1x, v1y = elastic_collision(self, i, t + self.t0)
                v2x, v2y = elastic_collision(i, self, t + self.t0)


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

    def draw(self):
        draw_circle(win, self.coords[0], self.coords[1], self.radius, self.color)





def draw_circle(surface, x, y, radius, color):
    x = int(x)
    y = int(y)
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def vector_angle(v):
    ba = np.array(v)
    dot = ba[0]
    det = ba[1]
    return math.atan2(det, dot)


def elastic_collision(ob1, ob2, t):
    g=1000
    t1 = t - ob1.t0
    t2 = t - ob2.t0

    v1y = g * t1 + ob1.vy
    v2y = g * t2 + ob2.vy

    theta1 = vector_angle([ob1.vx, v1y])
    theta2 = vector_angle([ob2.vx, v2y])

    dx = ob2.coords[0] - ob1.coords[0]
    if dx == 0:
        phi = math.pi / 2
    else:
        phi = math.atan((ob2.coords[1] - ob1.coords[1]) / dx)

    m1 = ob1.mass
    m2 = ob2.mass

    v1 = math.sqrt(ob1.vx * ob1.vx + v1y * v1y)
    v2 = math.sqrt(ob2.vx * ob2.vx + v2y * v2y)

    vx = (v1 * math.cos(theta1 - phi) * (m1 - m2) + 2 * m2 * v2 * math.cos(theta2 - phi)) / (m1 + m2)
    vy = vx

    vx = vx * math.cos(phi) + v1 * math.sin(theta1 - phi) * math.cos(phi + math.pi / 2)
    vy = vy * math.sin(phi) + v1 * math.sin(theta1 - phi) * math.sin(phi + math.pi / 2)
    return vx, vy


def spawn_ball(mouse_x, mouse_y, x, y):
    global click, clicked, init_ball, balls

    def speed(mouse_x, mouse_y, x, y):
        a = np.array([x, y])
        b = np.array([mouse_x, mouse_y])
        ba = a - b
        r = np.linalg.norm(ba)
        dot = ba[0]
        det = -ba[1]
        angle = math.atan2(det, dot)
        sin = math.sin(angle)
        cos = math.cos(angle)
        vx = r * cos * 4
        vy = -r * sin * 4
        return vx, vy

    if click and not clicked:
        clicked = True
        x, y = mouse_x, mouse_y
        init_ball = ball(mouse_x, mouse_y, 0, 0, time.time())
        init_ball.draw()
    elif click and clicked:
        init_ball.radius = int(20 * math.sin(time.time() * 2) + 20)
        init_ball.mass = init_ball.radius * init_ball.radius / 10
        pygame.draw.aaline(win, (255, 255, 255), (x, y), (mouse_x, mouse_y))
        init_ball.vx, init_ball.vy = speed(mouse_x, mouse_y, x, y)
        init_ball.draw()
    elif not click and clicked:
        clicked = False
        init_ball.t0 = time.time()
        balls.append(init_ball)
    return x, y


def main():
    global click,clicked,init_ball,balls,win

    flag = True
    myfont = pygame.font.SysFont('Arial', 30)
    textsurface2 = myfont.render(f'Press Q to exit', False, (255, 255, 255))
    win.blit(textsurface2, (300, 300))


    mouse_x, mouse_y,x,y = 0, 0, 0, 0
    balls = []
    init_ball = ball(0, 0, 0, 0, time.time())
    click,clicked = False,False

    while flag:
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                flag = False

        x, y = spawn_ball(mouse_x, mouse_y, x, y)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        click = False
        if pygame.mouse.get_pressed()[0]:
            click = True

        i = 0
        value_remove = 35
        if len(balls) > value_remove:
            print("===============ПРОИЗОШЛА ЧИСТКА ПОЛЯ==================")
            for i in range(value_remove):
                balls.pop(value_remove-i)

        while i in range(len(balls)):
            try:
                balls[i].draw()
                balls[i].update(time.time(), balls[i + 1:])
            except ZeroDivisionError:
                balls.pop(i)
                i -= 1
            i += 1

        pygame.display.update()

if __name__ == "__main__":
    width = 720
    height = 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("by Alexandrova Dasha")
    pygame.init()
    main()
    pygame.quit()