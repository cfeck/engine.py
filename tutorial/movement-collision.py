from engine import Game, Sprite


def frame():
    if not ball.inside(game.area):
        ball.vx = -ball.vx


game = Game()

ball = Sprite(40, 40)
ball.center_in(game.area)
ball.vx = 4
game.show(ball)

game.frame = frame
game.exec()

