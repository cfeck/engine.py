from engine import *


app = App()
conf = app.settings

print(conf.value("A"))
print(int(conf.value("B", 12)))
print(bool(conf.value("C")))
print(list(conf.value("D", [])))

conf.setValue("A", "123")
conf.setValue("B", 123)
conf.setValue("C", True)
conf.setValue("D", [1, 2, 3])

app.exec()

