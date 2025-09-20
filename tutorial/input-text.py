from engine import Game


def frame():
    game.background = game.input("Color: ")
    if game.background == '':
        game.quit()


game = Game()

game.frame = frame
game.exec()

