from engine import *


app = App()

emoji = Emoji(128512, 100)
gfx = emoji.graphics()

sprite = Sprite(gfx.w, gfx.h)
sprite.setGraphics(gfx)

sprite.center_in(app.area)
app.show(sprite)

app.exec()

