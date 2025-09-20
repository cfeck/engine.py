from engine import *

def frame():
    paddle_r.center_in(game.mouse)
    paddle_r.x = game.w - paddle_r.w

    if ball.hits(paddle_r) or ball.hits(paddle_l):
        ball.vx = -ball.vx

    if ball.x > paddle_r.x:
        ball.center_in(game.area)


game = Game()

ball = Sprite(24, 24)
ball.center_in(game.area)
ball.vx = 5
game.show(ball)

paddle_l = Sprite(24, 128)
paddle_l.center_in(game.area)
paddle_l.x = 0
game.show(paddle_l)

paddle_r = Sprite(24, 128)
paddle_r.center_in(game.area)
paddle_r.x = game.w - paddle_r.w
game.show(paddle_r)

for y in range(-20, 20):
    dot = Sprite(4, 4)
    dot.center_in(game.area)
    dot.y += game.h / 39 * y
    game.show(dot)

game.frame = frame
game.exec()

