from engine import App, Emoji


app = App()

emoji = Emoji('U+1F600', 60)
app.show(emoji)

app.exec()

