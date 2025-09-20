from engine import Game


def frame():
    name = game.input("Name: ")
    game.text = "Hallo " + name + "!"
    del game.frame


game = Game()

game.frame = frame
game.exec()

