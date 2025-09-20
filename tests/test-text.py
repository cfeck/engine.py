from engine import *


app = App()

app.text = "Text"

app.top.text = "Top\nText"
app.top.left = "Top\nLeft"
app.top.right = "Top\nRight"

app.bot.text = "Bot\nText"
app.bot.left = "Bot\nLeft"
app.bot.right = "Bot\nRight"

app.exec()

