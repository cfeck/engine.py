from engine import *
from random import randint


def frame():
    sx = wobbler.center().x
    sy = wobbler.center().y
    cx = game.mouse.x
    cy = game.mouse.y
    wobbler.ax = -0.05 * (sx - cx)
    wobbler.ay = -0.05 * (sy - cy)
    wobbler.vx *= 0.85
    wobbler.vy *= 0.85

    player.center_in(game.mouse)


game = Game()

player = Sprite(10, 10)
game.show(player)

wobbler = Sprite(40, 40)
game.show(wobbler)

game.frame = frame
game.exec()

