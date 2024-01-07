from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, x, y, speed, width, heigh):
        super().__init__()
        self.img = transform.scale(image.load(player_img), (width, heigh))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def right_player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < (mw_height - 80):
            self.rect.y += self.speed

    def left_player(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < (mw_height - 80):
            self.rect.y += self.speed

fon = (0, 0, 0)
mw_width = 600
mw_height = 500
mw = display.set_mode((mw_width, mw_height))
mw.fill(fon)

game = True
finish = False
clock = time.Clock()

fps = 60

racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)

ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()

font = font.Font(None, 35)

louse1 = font.render("1 player lose", True, (180, 0, 0))
louse2 = font.render("2 player lose", True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mw.fill(fon)
        racket1.left_player()
        racket2.right_player()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > mw_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            mw.blit(louse1, (200, 200))
            game_over = True
        if ball.rect.x > mw_width:
            finish = True
            mw.blit(louse2, (200, 200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)