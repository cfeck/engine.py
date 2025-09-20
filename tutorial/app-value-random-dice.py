from engine import App
import random


app = App()

wurf = random.randint(1, 6)
app.text = str(wurf)

app.exec()

