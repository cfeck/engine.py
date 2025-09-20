from engine import *


def frame():
    player.vx = 4 * game.kx
    player.vy = 4 * game.ky

    player.keep_in(game.area)


game = Game()

player = Sprite(40, 40)
game.show(player)

game.frame = frame
game.exec()

