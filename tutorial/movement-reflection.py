from engine import *


def frame():
    paddle.center_in(game.mouse)
    paddle.y = game.h - 30
    area = Area(680, 480)
    area.x = -20
    paddle.keep_in(area)

    if ball.x < 0 or ball.x > game.w - ball.w:
        ball.vx = -ball.vx
    if ball.y < 0:
        ball.vy = -ball.vy

    if ball.y > paddle.y - ball.h:
        if ball.hits(paddle):
            ball.vy = -ball.vy
            ball.vx = -0.1 * (paddle.center().x - ball.center().x)
        else:
            ball.center_in(game.area)
            ball.vx = 0
            ball.vy = -4


game = Game()

paddle = Sprite(128, 24)
paddle.y = game.h - 30
game.show(paddle)

ball = Sprite(24, 24)
ball.y = game.h
game.show(ball)

game.frame = frame
game.exec()

