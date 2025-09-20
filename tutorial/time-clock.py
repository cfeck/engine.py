from engine import *


def frame():
    game.clock += 1

    if game.key:
        game.clock = 0

    seconds = game.clock // game.fps
    minutes = seconds // 60
    seconds -= 60 * minutes

    game.text = str(minutes) + ":" + str(seconds).zfill(2)


game = Game()

game.clock = 0

game.frame = frame
game.exec()

