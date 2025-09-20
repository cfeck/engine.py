from engine import *


def frame():
    if game.key or game.mouse.pressed:
        player.vy = -5

    if player.y > game.h - player.h:
        player.y = game.h - player.h


game = Game()

player = Sprite(40, 40)
player.x = 320 - player.w / 2
player.ay = 0.25
game.show(player)

game.frame = frame
game.exec()

