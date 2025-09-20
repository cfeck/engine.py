from engine import *


def recolor(x, y, uniform):
    gfx = uniform[0]
    shift = uniform[1]

    rgba = gfx.pixel(x, y)
    rgb = QColor.fromRgba(rgba)
    hsv = rgb.toHsv()
    h = hsv.hue()
    if h < 10 or h > 350:
#    if h > 30 and h < 60:  # for emoji
        h += shift
        rgb.setHsv(h % 360, hsv.saturation(), hsv.value(), rgb.alpha() * 0.75)
        return rgb.rgba()
    else:
        return rgba


def frame():
    for sprite in sprites:
        if sprite.y < -50:
            shift = random.randint(-180, 180)
            gfx = Graphics(gfx_red)
            gfx.execShader(recolor, gfx, shift)
            sprite.setGraphics(gfx)
            sprite.vx = random.randint(-10, 10) / 30
            sprite.r = 12 + sprite.vx * 30
            sprite.z = random.randint(70, 140) / 100
            sprite.random_in(app.area)
            sprite.y = app.h
            sprite.vy = -2 * sprite.z


app = App()

app.background = "skyblue"

gfx_red = Graphics(Emoji('balloon', 32))

sprites = []
for n in range(20):
    sprite = Sprite(32, 32)
    sprite.y = -100
    sprites += [sprite]

app.show(sprites)

app.frame = frame
app.exec()

