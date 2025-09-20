from engine import *


def show_menu():
    app.show(shadow)
    app.show(menu)
    app.show(titlebg)
    app.show(title)
    app.show(selection)
    for i in range(5):
        app.show(texts[i])
    app.frame = handle_menu


def handle_menu():
    for i in range(5):
        if app.mouse.hits(texts[i]):
            app.current = i
        if i == app.current:
            texts[i].color = "white"
        else:
            texts[i].color = "black"
    selection.x = 185
    selection.y = 137 + 30 * app.current
    if app.mouse.pressed:
        app.frame = hide_menu


def hide_menu():
    app.hide(shadow)
    app.hide(menu)
    app.hide(titlebg)
    app.hide(title)
    app.hide(selection)
    for i in range(5):
        app.hide(texts[i])
    app.text = "Item " + str(app.current) + " selected"


app = Game()

app.background = "skyblue"

items = [ "Play against computer", "Play against yourself", "Settings", "About", "Quit" ]
no = len(items)

menu = Sprite(300, 200)
menu.corner_radius = 5
menu.color = "lightgray"
menu.x = 170
menu.y = 95

shadow = Sprite(300, 200)
shadow.corner_radius = 5
shadow.color = "black"
shadow.transparency = 0.8
shadow.x = 175
shadow.y = 100

titlebg = Sprite(290, 30)
titlebg.corner_radius = 5
titlebg.color = "gray"
titlebg.x = 175
titlebg.y = 100

title = Text(300, 30)
title.size = 20
title.x = 170
title.y = 100
title.color = "black"
title.text = "MAIN MENU"

texts = [0] * no

for i in range(no):
    text = Text(270, 20)
    text.size = 20
    text.x = 190
    text.y = 140 + 30 * i
    text.text = items[i]
    texts[i] = text

selection = Sprite(270, 30)
selection.color = "darkblue"
selection.corner_radius = 5

app.current = 0

app.frame = show_menu
app.exec()

