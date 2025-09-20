from engine import *


def slide_in():
    if table.vy > 0:
        app.frame = frame


def frame():
    app.top.text = "Highscore Table"
    table.vy = 0
    if table.pressed:
        app.frame = slide_out


def slide_out():
    app.top.text = ''
    if table.vy > 20:
        app.quit()


def makeHtmlTable(data, height):
    html  = '<table border cellpadding="5" width = "100%">'
    html += '<tr><th>Player Name</th><th>Score</th></tr>'
    for name, score in data.items():
        html += '<tr><td>' + name + '</td><td align="right">' + str(score) + '</td></tr>'
    for n in range(height - len(data)):
        html += '<tr><td>-</td><td align="right">-</td></tr>'
    html += '</table>'
    return html


app = Game()

app.background = RGB(20, 50, 50)

data = { "Dieter": 12, "Udo": 1000 }

surface = Sprite(320, 250)
surface.color = RGB(50, 100, 100)

shadow = Sprite(320, 250)
shadow.x = 10
shadow.y = 10
shadow.color = RGB(0, 0, 0, 100)

text = Text(320, 250)
text.color = "white"
text.html = True
text.text = makeHtmlTable(data, 5)

table = Group(320, 250)
table.center_in(app.area)
table.y += 200
table.vy = -16
table.ay = 0.5
table.sprites = [ shadow, surface, text ]
app.show(table)

app.frame = slide_in
app.exec()

