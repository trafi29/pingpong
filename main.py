from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, x, y, speed, width, heigh):
        super().__init__()
        self.img = transform.scale(image.load(player_img), (width, heigh))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect_x = x
        self.rect_y = y
    def reset(self):
        mw.blit(self.img, (self.rect_x, self.rect_y))

class Player(GameSprite):
    def right_player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect_y > 5:
            self.rect_y -= self.speed

        if keys[K_DOWN] and self.rect_y < (mw_heigh - 80):
            self.rect_y += self.speed

    def left_player(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect_y > 5:
            self.rect_y -= self.speed

        if keys[K_s] and self.rect_y < (mw_heigh - 80):
            self.rect_y += self.speed

fon = (0, 0, 0)
mw_width = 600
mw_heigh = 500
mw = display.set_mode((mw_width, mw_heigh))
mw.fill(fon)
