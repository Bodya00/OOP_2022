import pygame
from pygame.draw import *
pygame.init()
FPS=30
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((500, 350))
screen.fill('peachpuff')
#sun
def sun(a,b,c,x,y,r):
    '''
    Рисует солнце на небе.
    a,b,c - RGB цвет солнца
    x, y - координаты центра солнца
    r - радиус солнца
    '''
    circle(screen,(a,b,c),(x,y),r)
#land
def land(a,b,c,d):
    '''

        [(),(),..] - координаты x y для большого прямоугольника, являющегося землей
        d - толщина полоски, отвечающей за землю
    '''
    rect(screen,(a,b,c),[(0,300),(500,300)],d)
#cloud
def cloud(a,b,c,d):
    '''
        Рисует облака на небе.
        a,b,c - RGB цвет облака

    '''
    rect(screen,(a,b,c),[(0,150),(500,150,)],d)
#rock1
def rock(a,b,c):
    '''

    '''
    polygon(screen, (a, b, c), [(0, 200), (75, 110), (75, 110), (84, 127), (84, 127), (120, 120),
                                    (120, 120), (180, 180),
                                    (180, 180), (250, 170),
                                    (250, 170), (300, 190),
                                    (300, 190), (350, 200)], )
    polygon(screen, (a, b, c), [(360, 200), (400, 150),
                                    (400, 150), (450, 100),
                                    (450, 100), (500, 80), (500, 200)], )

# rock2
def rock2(a,b,c):
    '''
        Рисует гору.
        a,b,c - RGB цвет
        [(),(),..] - координаты x y для большого многоугольника, отвечающего за гору
        d - толщина полоски, отвечающей за землю
    '''
    polygon(screen, (a, b, c), [(0, 300), (75, 200), (75, 190), (84, 200), (84, 200), (120, 220),
                                  (120, 200), (180, 220),
                                  (180, 200), (250, 230),
                                  (250, 230), (300, 200), (310, 100),
                                  (320, 150), (350, 300)], )
    polygon(screen, (a, b, c), [(380, 300), (400, 200), (400, 300), (420, 250), (470, 200), (500, 150), (500, 300)])

def bird1(a, b, c ):
 '''
 a,b,c - RGB цвета из мейн файла
'''
line(screen, (0,0,0),
                 [100, 30],
                 [110, 15],3 )

line(screen, (0,0,0),
                 [100, 30],
                 [90, 15],3 )

def bird2(a, b, c ):
 '''
 a,b,c - RGB цвета из мейн файла
'''
line(screen, (0,0,0),
                 [140, 40],
                 [150, 25],3 )

line(screen, (0,0,0),
                 [140, 40],
                 [130, 25],3 )
def bird3(a, b, c ):
 '''
 a,b,c - RGB цвета из мейн файла
'''
line(screen, (0,0,0),
                 [200, 70],
                 [210, 55],3 )

line(screen, (0,0,0),
                 [200, 70],
                 [190, 55],3 )
def bird4(a, b, c ):
 '''
 a,b,c - RGB цвета из мейн файла
'''
line(screen, (0,0,0),
                 [350, 95],
                 [360, 70],3 )

line(screen, (0,0,0),
                 [350, 95],
                 [340, 70],3 )
def bird5(a, b, c ):
 '''
 a,b,c - RGB цвета из мейн файла
'''
line(screen, (0,0,0),
                 [400, 60],
                 [410, 45],3 )

line(screen, (0,0,0),
                 [400, 60],
                 [390, 45],3 )



