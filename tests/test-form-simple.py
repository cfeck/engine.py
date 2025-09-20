from engine import App, Form


def frame():
    form = Form()
    form.input_str("Name:")
    form.input_int("Alter:", maxval = 199)
    form.exec()
    if form.ok():
        app.text = form.Name + " " + str(form.Alter)
        del app.frame
    else:
        app.quit()


app = App()

app.frame = frame
app.exec()

