from engine import *


def frame():
    if player.x <= 0:
        player.vx = 5
    elif player.x >= 600:
        player.vx = -5


app = App()

head = Sprite(40, 40)
head.color = RGB(200, 150, 100)

body = Sprite(40, 160)
body.y = 40
body.color = RGB(100, 100, 200)

player = Group(40, 200)
player.x = 200
player.y = 200
player.vx = 5
player.sprites = [head, body]
app.show(player)

app.frame = frame
app.exec()

