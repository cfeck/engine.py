from engine import *


def frame():
    form = Form("Main Menu")
    font = form.font()
    font.setPointSize(font.pointSize() * 2)
    form.setFont(font)
    form.caption("Players")
    form.input_str("Name:", "Player")
    form.choice("Mode:", ["Play against Computer", "Play against Yourself"])
    form.caption("Settings")
    form.input_int("Difficulty:", minval = 1, maxval = 9)
    form.choice("Appearance:", ["Table", "Sand", "Grass", "Blue", "Retro"])
    form.exec()
    if form.ok():
        app.print(form.Mode)
    del app.frame


app = App()

app.frame = frame
app.exec()

