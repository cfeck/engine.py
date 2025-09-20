from engine import *


def frame1():
    name = app.input("Name:")
    alter = app.input("Alter:")
    alter = int(alter)
    app.print("Hallo " + name + "!")
    if alter > 12:
        app.print("Wie geht es Ihnen?")
    else:
        app.print("Wie geht es Dir?")
    del app.frame


def frame2():
    form = Form()
    form.input("Name:")
    form.input_int("Alter:")
    form.exec()
    if form.ok():
        app.print("Hallo " + form.Name + "!")
        if form.Alter > 12:
            app.print("Wie geht es Ihnen?")
        else:
            app.print("Wie geht es Dir?")
    del app.frame


app = App()

app.frame = frame2
app.exec()

