from engine import Game


def frame():
    game.text = str(round(game.time, 1))


game = Game()

game.frame = frame
game.exec()

