from engine import *


def frame():
    if game.key:
        player.vx = 4 * game.kx
        player.vy = 4 * game.ky

    player.vx *= 0.9
    player.vy *= 0.9


game = Game()

player = Sprite(40, 40)
game.show(player)

game.frame = frame
game.exec()

