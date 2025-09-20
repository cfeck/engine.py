from engine import Game


def frame():
    game.text = str(round(game.time, 1))


game = Game()
game.fps = 2

game.frame = frame
game.exec()

