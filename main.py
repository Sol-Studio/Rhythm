import pygame
from pygame.locals import *
import sys
import time
import random
from threading import Thread
from pynput.keyboard import Key, Listener
import ctypes

bg_color=(40,0,0)
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
    

    
    

colora, colors, colord, colorf = (0,0,0),(0,0,0),(0,0,0),(0,0,0)
colorh, colorj, colork, colorl = (0,0,0),(0,0,0),(0,0,0),(0,0,0)
tha = Thread(target=work, args=(200,colora, 97))
ths = Thread(target=work, args=(400,colors, K_s))
thd = Thread(target=work, args=(600,colord, K_d))
thf = Thread(target=work, args=(800,colorf, K_f))
thh = Thread(target=work, args=(1000,colorh, K_h))
thj = Thread(target=work, args=(1200,colorj, K_j))
thk = Thread(target=work, args=(1400,colork, K_k))
thl = Thread(target=work, args=(1600,colorl, K_l))


keys = []
pygame.init()
SURFACE = pygame.display.set_mode((1800,400))
pygame.display.set_caption("리듬을 가지고 놀기")
user32 = ctypes.windll.user32
FPSCLOCK = pygame.time.Clock()
while True:
    sysfont=pygame.font.SysFont(None, 70)
    #SURFACE.fill((255,255,255))
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            keys.append(event.key)
            
        if event.type == KEYUP:
            try:
                keys.remove(event.key)
            except:
                pass

        
    if 97 in keys:
        colora = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        tha.start()


    elif 115 in keys:
        colors = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        ths.start()



    elif 100 in keys:
        colord = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thd.start()


    elif 102 in keys:
        colorf = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thf.start()

    elif K_h in keys:
        colorh = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thh.start()

    elif K_j in keys:
        colorj = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thj.start()

    elif K_k in keys:
        colork = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thk.start()

    elif K_l in keys:
        colorl = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thl.start()

    elif K_SPACE in keys:
        key = 0
        bg_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        SURFACE.fill(bg_color)
        


    tha = Thread(target=work, args=(200,colora, 97))
    ths = Thread(target=work, args=(400,colors, K_s))
    thd = Thread(target=work, args=(600,colord, K_d))
    thf = Thread(target=work, args=(800,colorf, K_f))
    thh = Thread(target=work, args=(1000,colorh, K_h))
    thj = Thread(target=work, args=(1200,colorj, K_j))
    thk = Thread(target=work, args=(1400,colork, K_k))
    thl = Thread(target=work, args=(1600,colorl, K_l))

    pygame.display.update()
    

