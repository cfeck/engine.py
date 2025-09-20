from engine import *


def frame():
#    app.mouse.keep_in(app.area)

    app.top.text = "pressed = " + str(app.mouse.pressed)
    app.top.left = "x = " + str(app.mouse.x)
    app.top.right = "y = " + str(app.mouse.y)

    player.center_in(app.mouse)
    player.frame = app.mouse.pressed


app = App()

face0 = Emoji(128578, 64)
face1 = Emoji(129321, 64)
face2 = Emoji(128513, 64)
face3 = Emoji(128512, 64)

player = Sprite(64, 64)
player.setGraphics([face0, face1, face2, face3])
app.show(player)

app.frame = frame
app.exec()

