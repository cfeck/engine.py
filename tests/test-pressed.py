from engine import *


def frame():
    for block in blocks:
        if block.pressed:
            block.color = "white"
        else:
            block.color = "gray"


app = App()

blocks = []
for n in range(50):
    block = Sprite(40, 40)
    block.random_in(app.area)
    blocks.append(block)

app.show(blocks)

app.frame = frame
app.exec()

