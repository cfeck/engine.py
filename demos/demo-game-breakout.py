from engine import *
from random import randint


def frame():
    paddle.x = game.mouse.x
    area = Area(680, 480)
    area.x = -20
    paddle.keep_in(area)

    if ball.x < 160 or ball.x > game.w - 160 - 24:
        ball.vx = -ball.vx
        impact4.play()
    if ball.y < 0:
        ball.vy = -ball.vy
        ball.vx *= 1.1
        impact4.play()

    if ball.hits(block):
        ball.vx = -ball.vx
        ball.vy = -ball.vy
        impact4.play()

    if ball.hits(target):
        ball.y = 400
        ball.vy = -4
        target.x = randint(170, game.w - 170 - target.w)
        if target.x > 320:
            block.x = target.x - 100
        else:
            block.x = target.x + 100

    for coin in coins:
        if ball.hits(coin):
#            coin.animated = False
#            coin.x = -100
            coins.remove(coin)
            game.hide(coin)

    if ball.hits(hot):
        if not ball.hits_temp:
            if abs(ball.vy) < 8:
                ball.vx *= 2
                ball.vy *= 2
            ball.hits_temp = True
    elif ball.hits(cold):
        if not ball.hits_temp:
            if abs(ball.vy) > 1:
                ball.vx /= 2
                ball.vy /= 2
            ball.hits_temp = True
    else:
        ball.hits_temp = False

    if ball.y > paddle.y - 24:
        if ball.hits(paddle):
            ball.vy = -ball.vy
            ball.vx = -0.1 * (paddle.center().x - ball.center().x)
            impact3.play()
        else:
            ball.x = game.w / 2 - ball.w / 2
            ball.y = 0
            ball.vx = randint(-40, 40) / 10
            ball.vy = 4
            shutdown1.play()

#    if game.key:
#        ball.x += 5 * game.kx
#        ball.y += 5 * game.ky


class Block(Sprite):
    def __init__(b, x, y):
        Sprite.__init__(b, 32, 32)
        b.setSheetPos(40 * x, 40 * y)
        b.setShadow(8)


game = Game("BreakWall")
game.setCursorShape("blank")
game.setBackground("breakout_bg.png")
#game.setSprites("breakout_sprites(no shadow)_5.png")
game.setSpriteSheet("breakout_sprites_fixed.png")

impact3 = Sound("sfx_sounds_impact3.wav")
impact4 = Sound("sfx_sounds_impact4.wav")
shutdown1 = Sound("sfx_sound_shutdown1.wav")

paddle = Sprite(128, 24)
paddle.setSheetPos(40 * 0, 40 * 7)
paddle.setShadow(8)
#paddle.x = game.w / 2 - paddle.w / 2
paddle.y = game.h - 30
game.show(paddle)

ball = Sprite(24, 24)
ball.setSheetPos(40 * 4, 40 * 6)
ball.x = game.w / 2 - ball.w / 2
ball.y = 400
ball.vx = 0
ball.vy = -4
ball.hits_temp = False
game.show(ball)

block = Block(0, 0)
block.x = 400
block.y = 100
game.show(block)

target = Block(6, 0)
target.x = 450
target.y = 100
game.show(target)

hot = Block(6, 2)
hot.x = 200
hot.y = 200
game.show(hot)

cold = Block(5, 2)
cold.x = game.w - 200 - cold.w
cold.y = 200
game.show(cold)

coins = []
for i in range(4):
    coin = Animation(24, 24)
    coin.setSheetPos(0, 400 - 24)
    coin.frames = 16
    coin.x = randint(200, game.w - 200 - coin.w)
    coin.y = randint(10, 400)
    coin.frame = randint(0, 15)
    coin.ticks = randint(0, 2)
    coin.fps = 20
    coins.append(coin)
    game.show(coin)

game.frame = frame
game.exec()

