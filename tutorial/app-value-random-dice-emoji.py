from engine import App, Emoji
import random


app = App()

wurf = random.randint(1, 6)
app.text = Emoji("die face-" + str(wurf)).text

app.exec()

