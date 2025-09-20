from engine import *


def frame():
    conf = app.settings
    form = Form()
    form.input_str("Name:", conf.value("Name", "Player"))
    form.exec()
    if form.ok():
        conf.setValue("Name", form.Name)
    del app.frame


app = App("SettingsDemo")

app.frame = frame
app.exec()

