from engine import *


app = App()

for x, y in Grid(64, 48):
    text = Emoji(0x1F000 + x + 64 * y, 10)
    text.x = 10 * x
    text.y = 10 * y
    app.show(text)

app.exec()

