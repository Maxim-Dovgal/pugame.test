from pygame import *

window = display.set_mode((700, 500))
display.set_caption("дожени мене")
background = transform.scale(
        image.load('fon.png'),
        (700, 500)
    )

x1 = 300
y1 = 300
x2 = 200
y2 = 50
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
game = True
while game:
    window.blit(background, (0, 0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False 

    keys_pressed = key.get_pressed()

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

    clock.tick(FPS)
    display.update()
