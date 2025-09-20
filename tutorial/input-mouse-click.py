from engine import *


def frame():
    if game.mouse.pressed and game.mouse.hits(button):
        button.clicked = True

    if button.clicked:
        game.text = "OK!"
    else:
        game.text = "Click below!"


game = Game()

button = Sprite(200, 40)
button.center_in(game.area)
button.y += 100
button.clicked = False

game.show(button)

game.frame = frame
game.exec()

