from engine import Game


def frame():
    seconds = int(game.time)

    if seconds < 10:
        game.text = str(10 - seconds)
    else:
        game.text = "GO"


game = Game()

game.frame = frame
game.exec()

