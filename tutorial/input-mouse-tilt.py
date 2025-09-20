from engine import *


def frame():
    ball.ax = 0.003 * (game.mouse.x - game.w / 2)
    ball.ay = 0.003 * (game.mouse.y - game.h / 2)

    ball.vx *= 0.99
    ball.vy *= 0.99

    if ball.x < 0 or ball.x > game.w - ball.w:
        ball.x -= ball.vx
        ball.vx = -0.5 * ball.vx
        ball.ax *= 0.9

    if ball.y < 0 or ball.y > game.h - ball.w:
        ball.y -= ball.vy
        ball.vy = -0.5 * ball.vy
        ball.ay *= 0.9


game = Game()

center = Sprite(16, 16)
center.center_in(game.area)
game.show(center)

ball = Sprite(24, 24)
ball.center_in(game.area)
game.show(ball)

game.frame = frame
game.exec()

