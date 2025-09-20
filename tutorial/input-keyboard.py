from engine import *


def frame():
    app.top.text = "key = " + str(app.key)
    app.top.left = "kx = " + str(app.kx)
    app.top.right = "ky = " + str(app.ky)

    player.vx = app.kx
    player.vy = app.ky
    player.frame = app.key


app = App()

face0 = Emoji(128578, 64)
face1 = Emoji(129321, 64)

player = Sprite(64, 64)
player.setGraphics([face0, face1])
app.show(player)

app.frame = frame
app.exec()

