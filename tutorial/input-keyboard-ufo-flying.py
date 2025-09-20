from engine import *


def frame():
    player.ax = game.kx / 30
    player.ay = game.ky / 30

    player.keep_in(game.area)


game = Game()

player = Sprite(40, 40)
game.show(player)

game.frame = frame
game.exec()

