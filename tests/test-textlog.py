from engine import *


def frame():
    if app.time > app.nexttime:
        app.nexttime = app.time + 1
        log.text += "\nHallo"


app = App()

app.nexttime = app.time + 1

bg = Sprite(200, 200)
bg.x = 0
bg.y = 280
bg.color = RGB(50, 50, 50)
bg.transparency = 0.5
app.show(bg)

log = Text(200, 200)
log.x = 0
log.y = 280
log.color = RGB(250, 250, 250)
log.text = "Hallo"
log.size = 20
app.show(log)

app.frame = frame
app.exec()

