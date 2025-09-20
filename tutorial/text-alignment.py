from engine import App


app = App()

app.top.left = "top.left"
app.top.text = "top.text"
app.top.right = "top.right"

app.bot.left = "bot.left"
app.bot.text = "bot.text"
app.bot.right = "bot.right"

app.exec()

