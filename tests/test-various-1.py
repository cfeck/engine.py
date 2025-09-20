from engine import App, Text


app = App()

text = Text()
text.text = chr(128512)
text.x = 0
text.y = 0
text.moveTo(640, 480, 2)
app.show(text)

app.exec()

