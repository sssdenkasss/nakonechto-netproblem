from pygame import *

win_width = 700
win_height = 500
display.set_caption('Shooter')
window = display.set_mode((win_width, win_height))

img_back = 'galaxy.jpg'
img_hero ='rocket.png'

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

background = transform.scale(image.load(img_back), (win_width, win_height))
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))
        display.update()
    time.delay(50)













