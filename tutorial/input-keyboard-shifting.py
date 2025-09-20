from engine import *


def frame():
    if game.key:
        player.ax = game.kx / 10
        player.ay = game.ky / 10
    else:
        player.ax = 0
        player.ay = 0
        player.vx *= 0.8
        player.vy *= 0.8

    player.keep_in(game.area)


game = Game()

player = Sprite(40, 40)
game.show(player)

game.frame = frame
game.exec()

