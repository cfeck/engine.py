from engine import *
from random import randint


def frame():
    if player.y < 0 or player.y > game.h - player.h:
        player.y -= player.vy
        player.vy *= -1
        player.vx *= 0.9
        player.vy *= 0.9
    if player.x > game.w - player.w or player.x < 0:
        player.x -= player.vx
        player.vx *= -1
        player.vx *= 0.9
        player.vy *= 0.9

    player.vx *= 0.99
    player.vy *= 0.99

    if abs(player.vx) < 0.03 or abs(player.vy) < 0.03:
        player.vx = randint(-50, 50)
        player.vy = randint(-50, 50)


game = Game()

player = Sprite(24, 24)
game.show(player)

game.frame = frame
game.exec()

