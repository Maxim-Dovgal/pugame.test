#імпорт вісіх елементів пігейм
from pygame import *
#створення вікна
window = display.set_mode((700, 500))
#підпис вікна
display.set_caption("дожени мене")
#1.завантаження картинки 2. зміна розміру до вікна
background = transform.scale(
        image.load('fon.png'),
        (700, 500)
    )

x1 = 300
y1 = 300
x2 = 200
y2 = 50
#годиник
clock = time.Clock()
FPS = 120
speed = 10
sprite1 = transform.scale(
        image.load('t-34.png'),
        (100, 35)
)
sprite2 = transform.scale(
        image.load('t-34.png'),
        (100, 35)
)
#вимикач гри
game = True
#ігровий цикл
while game:
        #відмалювання фону з кординатами 0 0
    window.blit(background, (0, 0))
    #перебір поточних подій
    for e in event.get():
            #перевіряємо чи натиснуто хрестик
        if e.type == QUIT:
        #гра закривається
            game = False 
        #натиснуті клавіші
    keys_pressed = key.get_pressed()
#підключання клавіш з перевіркою чи невиходить за межі екрану
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 460:
        y1 += speed






    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
        #відрахування фпс
    clock.tick(FPS)
        #онувлювати екран
    display.update()
