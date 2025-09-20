from engine import *


def intro():
    app.text = "Verlasse nicht den Raum!"
    if app.time > 2 or app.key:
        app.frame = start


def start():
    app.text = ""
    smiley.text = chr(128512)
    smiley.center_in(app.area)
    app.show(smiley)
    app.frame = play


def play():
    smiley.x += 3 * app.kx
    smiley.y += 3 * app.ky
    if not smiley.inside(app.area):
        app.frame = game_over


def game_over():
    app.hide(smiley)
    app.text = ""
    app.print("***  GAME OVER  ***")
    app.print("Press Esc to quit")
    app.print("or Space to try again")
    if app.key:
        app.frame = start


app = App()

smiley = Text(20, 20)

app.frame = intro

app.exec()
