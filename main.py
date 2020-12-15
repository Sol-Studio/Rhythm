import pygame, sys, time, random
from pygame.locals import *
from threading import Thread
from pynput.keyboard import Key, Listener

def work(x,a,key):
    global bg_color, keys
    keys.remove(key)
    for i in range(20):
        time.sleep(0.004)
        pygame.draw.circle(SURFACE,a,(x,200),i*8)
        pygame.display.update()

    for i in range(20):
        time.sleep(0.004)
        pygame.draw.circle(SURFACE,bg_color,(x,200),152-(i*8)+10)
        pygame.draw.circle(SURFACE,a,(x,200),152-(i*8))
        pygame.display.update()
    

def random_color():
    return (random.randint(20,255),random.randint(20,255),random.randint(20,255))


colora, colors, colord, colorf,colorh, colorj, colork, colorl, bg_color= (0,0,0), (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)
keys = []
pygame.init()
SURFACE = pygame.display.set_mode((1800,400))
pygame.display.set_caption("내가 왜 이걸 만들고 있는건지도 모르겠는 그런 프로그램")
FPSCLOCK = pygame.time.Clock()
sysfont=pygame.font.SysFont(None, 70)

while True:
    tha = Thread(target=work, args=(200,colora, 97))
    ths = Thread(target=work, args=(400,colors, K_s))
    thd = Thread(target=work, args=(600,colord, K_d))
    thf = Thread(target=work, args=(800,colorf, K_f))
    thh = Thread(target=work, args=(1000,colorh, K_h))
    thj = Thread(target=work, args=(1200,colorj, K_j))
    thk = Thread(target=work, args=(1400,colork, K_k))
    thl = Thread(target=work, args=(1600,colorl, K_l))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bg_color = random_color()
                SURFACE.fill(bg_color)
                time.sleep(0.09)
            keys.append(event.key)
            
        if event.type == KEYUP:
            try:
                keys.remove(event.key)
            except:
                pass

    if 97 in keys:
        colora = random_color()
        tha.start()


    elif 115 in keys:
        colors = random_color()
        ths.start()

    elif 100 in keys:
        colord = random_color()
        thd.start()

    elif 102 in keys:
        colorf = random_color()
        thf.start()

    elif K_h in keys:
        colorh = random_color()
        thh.start()

    elif K_j in keys:
        colorj = random_color()
        thj.start()

    elif K_k in keys:
        colork = random_color()
        thk.start()

    elif K_l in keys:
        colorl = random_color()
        thl.start()

    elif K_SPACE in keys:
        key = 0
        bg_color = random_color()
        SURFACE.fill(bg_color)
