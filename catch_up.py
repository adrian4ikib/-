from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Догонялки")
#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))
clock = time.Clock()
FPS = 60
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

x1 = 100
y1 = 300

x2 = 300
y2 = 300

game = True
#обработай событие «клик по кнопке "Закрыть окно"»
while game:
    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    print(clock.get_fps())
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()
    if keys[K_LEFT] and x1 >5:
        x1 -= 10
    if keys[K_RIGHT] and x1 <595:
        x1 += 10
    if keys[K_UP] and y1 >5:  
        y1 -= 10
    if keys[K_DOWN] and y1 <595:
        y1 += 10

    if keys[K_a] and x2 >5:
        x2 -= 10
    if keys[K_d] and x2 <595:
        x2 += 10
    if keys[K_w] and y2 >5:  
        y2 -= 10
    if keys[K_s] and y2 <595:
        y2 += 10   


    clock.tick(FPS)
    display.update()