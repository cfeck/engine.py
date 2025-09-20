from engine import *


def wheel_event(e):
    delta = e.angleDelta().y() / 120
    player.y += 10 * delta


def frame():
    app.top.text = "Scroll mouse wheel"


app = App()

app.window.wheelEvent = wheel_event

player = Emoji(128512, 40)
player.center_in(app.area)
app.show(player)

app.frame = frame
app.exec()

