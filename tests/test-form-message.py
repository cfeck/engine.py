from engine import *

def frame():
    form = Form()
    form.caption("Quit App?")
    form.exec()
    if form.ok():
        app.quit()


app = App()

app.frame = frame
app.exec()

