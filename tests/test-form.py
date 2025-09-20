from engine import *

def start():
    form = Form()
    form.caption("Persönliche Daten")
    form.input_str("Vorname:")
    form.input_str("Name:")
    form.input_int("Alter:", 12)
    form.input_float("Größe:", 1.5)
    form.input_bool("Mädchen")
    form.input_bool("Junge")
    form.choice("Beruf", ["Kind", "Schüler", "Azubi", "Student", "Arbeiter", "Rentner"])
    form.separator()
    form.caption("Kontakt")
    form.input_str("Mail:")
    form.input_str("Telefon:")
    form.input_text("Adresse:")
    form.exec()
    if form.ok():
        app.print("Name: " + form.Vorname + " " + form.Name)
        app.print("Alter: " + str(form.Alter))
        app.print("Größe: " + str(form.Größe))
        app.print("Beruf: " + form.Beruf)
        app.print("Adresse: " + form.Adresse)
        del app.frame

app = App()
app.frame = start
app.exec()

