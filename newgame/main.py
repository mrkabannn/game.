from pygame import *
from random import randint

init()

win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
background = transform.scale(image.load("textur-gas-kvas-com-y97j-p-teksturi-doroga-dvukhpolosnaya-1.jpg"),(win_width, win_height))

speed = 10

mixer.init()
mixer.music.load("phonk-167055.mp3")
mixer.music.play()

clock = time.Clock()

max_lost = 6
lost = 0
number = 0
font.init()
font1 = font.Font(None, 36)
goal = 6

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (35, 35))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_UP]:
            self.rect.y += self.speed
        if keys [K_DOWN]:
            self.rect.y -= self.speed
        if keys [K_RIGHT]:
            self.rect.x += self.speed
        if keys [K_LEFT]:
            self.rect.x -= self.speed

player = Player("gratis-png-auto-laferrari-auto-racing-camioneta-vista-superior.png", 280, 0, speed)
finish = GameSprite("pngtree-realistic-style-racing-black-and-white-flag-png-image_2260545.jpg", 250, 700, 0)
walls = sprite.Group()

for i in range(1, 8):
    wall = GameSprite("pngtree-brown-house-wall-bricks-brick-realistic-real-png-image_3230087.jpg", randint())
    walls.add(wall)


display.update()
clock.tick(60)

quit()

