from engine import *


def key_event(e):
    code = e.key() - 2 ** 24
    if code >= 0:
        app.text = "Code: " + str(code)
        # handles Cursor, Esc, and Pause keys
        Window.keyPressEvent(app.window, e)
    else:
        app.text = "Text: " + e.text()


def frame():
    app.top.text = "Press any key"
    player.x += 2 * app.kx
    player.y += 2 * app.ky


app = App()

app.window.keyPressEvent = key_event

player = Emoji(128512, 40)
player.center_in(app.area)
app.show(player)

app.frame = frame
app.exec()

