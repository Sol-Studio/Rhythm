import pygame
from pygame.locals import QUIT, KEYDOWN, K_a,K_s,K_d,K_f,K_SPACE,FULLSCREEN
import sys
import time
import random
from threading import Thread
from pynput.keyboard import Key, Listener
import ctypes

bg_color=(40,0,0)
def work(x,a):
    global bg_color, key
    key = 0
    for i in range(20):
        pygame.draw.circle(SURFACE,a,(x,200),i*8)
        pygame.display.update()



    for i in range(20):

        SURFACE.fill(bg_color)

        pygame.draw.circle(SURFACE,a,(x,200),152-(i*8))
        pygame.display.update()


    
    

colora, colors, colord, colorf = (0,0,0),(0,0,0),(0,0,0),(0,0,0)
tha = Thread(target=work, args=(200,colora))
ths = Thread(target=work, args=(400,colors))
thd = Thread(target=work, args=(600,colord))
thf = Thread(target=work, args=(800,colorf))



key = 0
pygame.init()
SURFACE = pygame.display.set_mode((1000,400))
pygame.display.set_caption("리듬을 가지고 놀기")
user32 = ctypes.windll.user32
FPSCLOCK = pygame.time.Clock()
while True:
    sysfont=pygame.font.SysFont(None, 70)
    #SURFACE.fill((255,255,255))
    for event in pygame.event.get():
        '''
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        '''
        if event.type == KEYDOWN:
            key = event.key

    '''
    SURFACE.blit(sysfont.render("a",True,(0,0,0)), (150,400))    
    SURFACE.blit(sysfont.render("s",True,(0,0,0)), (320,400))  
    SURFACE.blit(sysfont.render("d",True,(0,0,0)), (470,400))  
    SURFACE.blit(sysfont.render("f",True,(0,0,0)), (620,400))  

    '''

        
    if key == 97:

        colora = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        tha.start()


    elif key == 115:

        colors = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        ths.start()



    elif key == 100:

        colord = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thd.start()


    elif key == 102:

        colorf = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
        thf.start()

    elif key == K_SPACE:
        key = 0
        bg_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        SURFACE.fill(bg_color)
        


    tha = Thread(target=work, args=(200,colora))
    ths = Thread(target=work, args=(400,colors))
    thd = Thread(target=work, args=(600,colord))
    thf = Thread(target=work, args=(800,colorf))


    pygame.display.update()
    

