import math
import time
import numpy as np
import pygame

import Ball,Const

def spawn_ball(mouse_x, mouse_y, x, y):
    global click, clicked, init_ball, balls,screen
    def speed(mouse_x, mouse_y, x, y):
        s = np.array([x, y]) - np.array([mouse_x, mouse_y]) #разница координат
        norm = np.linalg.norm(s) #вычислим норму разниц координат
        angle = math.atan2(-s[1], s[0]) #угол между разницей
        vx = norm * math.cos(angle) * 3
        vy = -norm * math.sin(angle) * 3
        return vx, vy
    if click and not clicked:
        #хотим создать шарик
        clicked = True
        x, y = mouse_x, mouse_y
        init_ball = Ball.ball(mouse_x, mouse_y, 0, 0, time.time(), screen)
        screen = init_ball.draw()
    elif click and clicked:
        #держим мышь и регулируется шарик (его параметры относительно нажатия)
        init_ball.radius = int(20 * math.sin(time.time()*2.05) + 20)
        init_ball.m = (4/3)*math.pi*math.pow(init_ball.radius,3)*init_ball.p
        init_ball.vx, init_ball.vy = speed(mouse_x, mouse_y, x, y)
        pygame.draw.aaline(screen, (255,255, 255), (x, y), (mouse_x, mouse_y))
        screen = init_ball.draw()
    elif not click and clicked:
        #отпустили мышь, шарик начинает движение
        clicked = False
        init_ball.t0 = time.time()
        balls.append(init_ball)
    return x, y

def main():
    global clicked,click,balls, init_ball,screen

    #============================Параметры игры
    width = Const.const.getparam()[1]
    height = Const.const.getparam()[0]
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("by Alexandrova Dasha")

    value_remove = 15
    flag,click,clicked = True, False, False
    mouse_x, mouse_y, x, y = 0,0,0,0
    balls = []
    init_ball = Ball.ball(0, 0, 0, 0, time.time(),screen)
    #=============================Процесс
    while flag:
        screen.fill((0, 0, 0))
        myfont = pygame.font.SysFont('Arial', 30)
        textsurface2 = myfont.render(f'Вместимость: {value_remove}', False, (255, 255, 255))
        screen.blit(textsurface2, (5, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                print("===============ИГРА ОКОНЧЕНА==================" + "\n" * 5)
                print("===============ИГРА ОКОНЧЕНА==================")
                flag = False

        x, y = spawn_ball(mouse_x, mouse_y, x, y)


        click = False
        if pygame.mouse.get_pressed()[0]:
            click = True
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if len(balls) > value_remove:
            print("===============ПРОИЗОШЛА ЧИСТКА ПОЛЯ=================="+"\n"*5)
            print("===============ПРОИЗОШЛА ЧИСТКА ПОЛЯ==================")
            for i in range(value_remove):
                balls.pop(value_remove - i)

        i = 0
        while i in range(len(balls)):
            try:
                balls[i].draw()
                balls[i].update(time.time(), balls[i + 1:])
            except Exception as e:
                print(e)
                balls.pop(i)
                i -= 1
            i += 1
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()