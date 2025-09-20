from engine import *


def frame():
    if player.y == player.ground:
        if game.kx:
            player.vx = 3 * game.kx
        else:
            if game.key:
                player.vy = -10
                player.ay = 0.25

    if player.y > player.ground:
        player.y = player.ground
        player.ay = 0
        player.vy = 0


game = Game()

player = Sprite(40, 40)
player.ground = game.h - player.h
player.vx = 3
player.y = player.ground
game.show(player)

game.frame = frame
game.exec()

