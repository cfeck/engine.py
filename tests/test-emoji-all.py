from engine import *


app = App()

for y in range(48):
    for x in range(64):
        text = Emoji(0x1F000 + x + 64 * y, 10)
        text.x = 10 * x + 5
        text.y = 10 * y + 5
        app.show(text)

app.exec()

