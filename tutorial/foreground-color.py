from engine import *


app = App()

app.background = "skyblue"

sprite1 = Sprite(100, 100)
sprite1.color = "red"
sprite1.x = 20
sprite1.y = 20
app.show(sprite1)

sprite2 = Sprite(100, 100)
sprite2.color = "green"
sprite2.x = 220
sprite2.y = 20
app.show(sprite2)

app.exec()

