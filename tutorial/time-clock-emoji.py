from engine import *


def frame():
    clock = int(app.time * 12) % 12
    names = ["TWELVE", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN"]
    app.text = Emoji("CLOCK FACE " + names[clock] + " OCLOCK").text


app = App()

app.clock = 0

app.frame = frame
app.exec()

