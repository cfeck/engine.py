##############################################################################
#
#  engine.py - Simple App/Game Engine for Python Qt
#

MODULE_NAME = "engine.py"
MODULE_VERSION = "0.1"
MODULE_COPYRIGHT = "Copyright 2025, Christoph Feck"
MODULE_LICENSE = "GNU GPL version 3"
MODULE_MAIL = "appengine/maxiom.de"
MODULE_URL = "github.com/cfeck/engine.py"


##############################################################################
#
#  imports
#

import math
import os
import platform
import random
import sys
import unicodedata


##############################################################################
#
#  import Qt
#

import importlib.util

def hasQtModule(name):
    try:
        loader = importlib.util.find_spec(qtmodule + ".Qt" + name)
        return loader is not None
    except:
        return False

def importQtSymbols(name, syms):
    mod = __import__(qtmodule + ".Qt" + name, None, None, syms)
    for sym in syms:
        globals()[sym] = getattr(mod, sym)

for qtmodule in ["PySide6", "PyQt6", "PySide2", "PyQt5", None]:
    if qtmodule and hasQtModule("Widgets"):
        break

if not qtmodule:
    print("Python Qt not installed")
    quit()

def importQt():
    implist = [
    ["Core",    ["Qt", "QSize", "QRectF", "QUrl", "QSettings"]],
    ["Gui",     ["QPainter", "QColor", "QImage", "QCursor", "qRgb", "qRgba", "qGray", "QPalette",
                 "QTextDocument", "QAbstractTextDocumentLayout"]],
    ["Widgets", ["QApplication", "QWidget",
                 "QDialog", "QInputDialog", "QFormLayout", "QVBoxLayout", "QDialogButtonBox", "QWidgetItem", "QLabel", "QFrame",
                 "QLineEdit", "QCheckBox", "QRadioButton", "QPlainTextEdit", "QComboBox", "QSpinBox", "QDoubleSpinBox"]],
    ]
    for imp in implist:
        importQtSymbols(imp[0], imp[1])

importQt()


##############################################################################
#
#  Utilities
#

def makeqcolor(x):
    if isinstance(x, QColor):
        return x
    if isinstance(x, int):
        return QColor.fromRgba(x)
    if isinstance(x, str):
        return QColor(x)
    if isinstance(x, list) or isinstance(x, tuple):
        if len(x) == 4:
            return QColor(x[0], x[1], x[2], x[3])
        return QColor(x[0], x[1], x[2])


def makeqimage(x):
    if isinstance(x, QImage):
        return x
    if isinstance(x, str):
        return QImage("assets/gfx/" + x)
    if isinstance(x, Text):
        return x.graphics()


class Grid:
    def __init__(g, w, h):
        g.w = w
        g.h = h
        g.cells = [ None ] * (w * h)

    def __getitem__(g, xy):
        return g.cells[xy[0] + xy[1] * g.w]

    def __setitem__(g, xy, v):
        g.cells[xy[0] + xy[1] * g.w] = v

    def __iter__(g):
        for y in range(g.h):
            for x in range(g.w):
                yield x,y


class RGB(QColor):
    def R(c):   return c.red()
    def G(c):   return c.green()
    def B(c):   return c.blue()
    def A(c):   return c.alpha()


##############################################################################
#
#  Graphics
#

class Graphics(QImage):
    def __init__(p, fn):
        if isinstance(fn, tuple):
            QImage.__init__(p, fn[0], fn[1], QImage.Format.Format_ARGB32)
        else:
            QImage.__init__(p, makeqimage(fn))
        p.w = p.width()
        p.h = p.height()
        p.convertTo(QImage.Format.Format_ARGB32)

    def mirrored(p):
        return Graphics(p.flipped(Qt.Orientation.Horizontal))

    def mirror(p):
        p.flip(Qt.Orientation.Horizontal)

    def replaceRgba(p, qrgba1, qrgba2):
        for y in range(p.height()):
            for x in range(p.width()):
                if p.pixel(x, y) == qrgba1:
                    p.setPixel(x, y, qrgba2)

    def replaceColor(p, color1, color2):
        qrgba1 = makeqcolor(color1).rgba()
        qrgba2 = makeqcolor(color2).rgba()
        p.replaceRgba(qrgba1, qrgba2)

    def makeTransparent(p, color = None):
        if color == None:
            qrgba = p.pixel(0, 0)
        else:
            qrgba = makeqcolor(color).rgba()
        p.replaceRgba(qrgba, qRgba(0, 0, 0, 0))

    def execShader(p, shader, *uniform):
        for y in range(p.height()):
            for x in range(p.width()):
                p.setPixel(x, y, shader(x, y, uniform))

    def execShaderArea(p, area, shader, *uniform):
        for y in range(area.y, area.y + area.h):
            for x in range(area.x, area.x + area.w):
                p.setPixel(x, y, shader(x, y, uniform))

    def shaded(p, shader, *uniform):
        p_shaded = QImage(p.size(), QImage.Format.Format_ARGB32)
        for y in range(p.height()):
            for x in range(p.width()):
                p_shaded.setPixel(x, y, shader(x, y, uniform))
        return Graphics(p_shaded)

    def execPainter(p, painter, *uniform):
        qpainter = QPainter(p)
        painter(qpainter, uniform)
        qpainter.end()


##############################################################################
#
#  Area
#

class Area:
    def __init__(a, w, h):
        a.x = 0
        a.y = 0
        a.w = w
        a.h = h
        a.pressed = 0

    def center(a):
        center = Area(0, 0)
        center.x = a.x + a.w / 2
        center.y = a.y + a.h / 2
        return center

    def center_in(a, a_in):
        a.x = a_in.x + a_in.w / 2 - a.w / 2
        a.y = a_in.y + a_in.h / 2 - a.h / 2

    def random_in(a, a_in):
        a.x = random.randint(a_in.x, a_in.x + a_in.w - a.w)
        a.y = random.randint(a_in.y, a_in.y + a_in.h - a.h)

    def keep_in(a, a_in):
        a.x = max(a.x, a_in.x)
        a.y = max(a.y, a_in.y)
        a.x = min(a.x, a_in.x + a_in.w - a.w)
        a.y = min(a.y, a_in.y + a_in.h - a.h)

    def inside(a, a_in):
        r1 = QRectF(a.x, a.y, a.w, a.h)
        r2 = QRectF(a_in.x, a_in.y, a_in.w, a_in.h)
        return r2.contains(r1)

    def hits(a1, a2):
        r1 = QRectF(a1.x, a1.y, a1.w, a1.h)
        r2 = QRectF(a2.x, a2.y, a2.w, a2.h)
        return r1.intersects(r2)


##############################################################################
#
#  Sprite
#

class Sprite(Area):
    def __init__(s, w, h):
        Area.__init__(s, w, h)
        s.sx = 0
        s.sy = 0
        s.ew = 0
        s.eh = 0
        s.gfx = None
        s.animated = False
        s.frames = 1
        s.frame = 0
        s.ticks = 0
        s.fps = 0
        s.stop()
        # transforms
        s.z = 1
        s.zx = 1
        s.zy = 1
        s.r = 0

    def setGraphics(s, gfx):
        if isinstance(gfx, list) or isinstance(gfx, tuple):
            s.animated = True
            s.frames = len(gfx)
            l = []
            for f in gfx:
                l.append(makeqimage(f))
            s.gfx = l
        else:
            s.gfx = makeqimage(gfx)

    def setSheetPos(s, x, y):
        s.sx = x
        s.sy = y

    def setShadow(s, shadow):
        s.ew = shadow
        s.eh = shadow

    def stop(s):
        s.vx = 0
        s.vy = 0
        s.ax = 0
        s.ay = 0

    def moveBy(s, dist, angle, time):
        angle = angle / 360 * 2 * math.pi
        x = s.x + dist * math.cos(angle)
        y = s.y + dist * math.sin(angle)
        s.moveTo(x, y, time)

    def moveTo(s, x, y, time):
        if time < 0.01:
            s.x = x
            s.y = y
        else:
            s.vx = (x - s.x) / (time * 60)
            s.vy = (y - s.y) / (time * 60)
            s.ax = 0
            s.ay = 0


class Animation(Sprite):
    def __init__(s, w, h):
        Sprite.__init__(s, w, h)
        s.animated = True
        s.fps = 20


class Group(Sprite):
    def __init__(g, w, h):
        Sprite.__init__(g, w, h)
        g.sprites = []


class Text(Sprite):
    def __init__(t, w = 0, h = 0):
        Sprite.__init__(t, w, h)
        t.text = ''
        t.left = ''
        t.right = ''
        t.outline = Qt.GlobalColor.black
        t.size = max(h, 20)

    def graphics(t):
        gfx = Graphics((t.w, t.h))
        gfx.fill(Qt.GlobalColor.transparent)
        p = QPainter(gfx)
        f = p.font()
        f.setPixelSize(int(t.size))
        p.setFont(f)
        p.drawText(gfx.rect(), Qt.AlignmentFlag.AlignCenter, t.text)
        p.end()
        return gfx


class Emoji(Text):
    def __init__(t, code = 0x1F600, size = 32):
        Text.__init__(t, size, size)
        t.size = size
        if isinstance(code, str):
            if len(code) > 0 and code[0] > 'z':
                t.text = code
            elif len(code) > 5 and code[:2] == "U+":
                t.text = chr(int(code[2:], 16))
            else:
                t.text = unicodedata.lookup(code)
        elif isinstance(code, int):
            t.text = chr(code)
        else:
            t.text = chr(0xFFFD)
        t.text += chr(0xFE0F)

    def name(t):
        return unicodedata.name(t.text[0])


##############################################################################
#
#  Sound
#

class SoundOff:
    def __init__(s, fn):
        fh = open("assets/sfx/" + fn, "rb")
        fh.close()
        pass

    def stop(s):
        pass

    def isPlaying(s):
        return False

    def play(s):
        pass

    def setVolume(s, volume):
        pass

if hasQtModule("Multimedia"):
    importQtSymbols("Multimedia", ["QSoundEffect"])

    # https://allanchain.github.io/blog/post/qt-sound-error/
    if platform.system() == 'Windows':
        # fix ffmpeg bug: [SWR] Output channel layout "" is invalid or unsupported.
        os.environ['QT_MEDIA_BACKEND'] = 'windows'

    class SoundOn(QSoundEffect):
        def __init__(s, fn):
            QSoundEffect.__init__(s)
            s.setSource(QUrl.fromLocalFile("assets/sfx/" + fn))
else:
    print("No QtMultimedia, Sound disabled")
    SoundOn = SoundOff

Sound = SoundOff


##############################################################################
#
#  Window
#

class Window(QWidget):
    def __init__(w):
        QWidget.__init__(w)
        w.setAutoFillBackground(False)
        w.setMouseTracking(True)
        w.sprites = []
        w.timer = None
        w.frame = 0

    def showEvent(w, e):
        if w.timer:
            w.killTimer(w.timer)
        w.timer = w.startTimer(1000 // w.app.fps)
        if hasattr(w.app, "init"):
            w.app.init()

    def hideEvent(w, e):
        if w.timer:
            w.killTimer(w.timer)
            w.timer = None

    def pause(w):
        if w.timer:
            w.killTimer(w.timer)
            w.timer = None
        else:
            w.timer = w.startTimer(1000 // w.app.fps)
        w.update()

    def keyControl(w, kx, ky):
        w.app.kx = kx
        w.app.ky = ky
        w.app.key = 1

    def keyPressEvent(w, e):
        k = e.key()
        if k >= 1 << 24:
            k -= 1 << 24
            if k == 8:      w.pause()
            elif k == 18:   w.keyControl(-1,  0)
            elif k == 19:   w.keyControl( 0, -1)
            elif k == 20:   w.keyControl( 1,  0)
            elif k == 21:   w.keyControl( 0,  1)
            elif k == 0:    w.close()
        else:
            k = chr(k)
            if k == 'P':    w.pause()
            elif k == 'W':  w.keyControl( 0, -1)
            elif k == 'A':  w.keyControl(-1,  0)
            elif k == 'S':  w.keyControl( 0,  1)
            elif k == 'D':  w.keyControl( 1,  0)
            else:           w.keyControl( 0,  0)

    def keyReleaseEvent(w, e):
        w.app.key = 0

    def mousePressEvent(w, e):
        if e.button() == Qt.MouseButton.LeftButton:
            w.app.mouse.pressed = 1
        elif e.button() == Qt.MouseButton.RightButton:
            w.app.mouse.pressed = 2
        else:
            w.app.mouse.pressed = 3
        pos = w.mapFromGlobal(QCursor.pos()) / w.scale
        w.app.mouse.x = pos.x()
        w.app.mouse.y = pos.y()
        for s in reversed(w.sprites):
            if w.app.mouse.hits(s):
                s.pressed = w.app.mouse.pressed
                break

    def mouseReleaseEvent(w, e):
        w.app.mouse.pressed = 0
        for s in w.sprites:
            s.pressed = 0

    def paintBackground(w, p):
        if hasattr(w, "bg"):
            p.drawImage(0, 0, w.bg)
        else:
            if hasattr(w.app, "background"):
                p.fillRect(w.rect(), makeqcolor(w.app.background))
            else:
                p.fillRect(w.rect(), QColor(0, 0, 0))

    def fgColor(w):
        color = QColor(255, 255, 255)
        if hasattr(w.app, "background"):
            if qGray(makeqcolor(w.app.background).rgb()) > 176:
                color = QColor(0, 0, 0)
        return color

    def paintSprite(w, p, s):
        gfx = s.gfx
        if hasattr(s, "transparency"):
            p.setOpacity(1.0 - s.transparency)
        if gfx == None:
            if hasattr(w, "fg"):
                gfx = w.fg
            else:
                color = w.fgColor()
                corner_radius = 0
                if not hasattr(w.app, "debug") or not w.app.debug:
                    if hasattr(s, "color"):
                        color = makeqcolor(s.color)
                    if hasattr(s, "corner_radius"):
                        corner_radius = s.corner_radius
                if corner_radius < 0:
                    p.setRenderHints(QPainter.RenderHint.Antialiasing, True)
                    p.setBrush(color)
                    p.setPen(Qt.PenStyle.NoPen)
                    p.drawEllipse(QRectF(0, 0, s.w, s.h))
                elif corner_radius > 0:
                    p.setRenderHints(QPainter.RenderHint.Antialiasing, True)
                    p.setBrush(color)
                    p.setPen(Qt.PenStyle.NoPen)
                    p.drawRoundedRect(QRectF(0, 0, s.w, s.h), corner_radius, corner_radius)
                else:
                    p.fillRect(QRectF(0, 0, s.w, s.h), color)
                return
        if hasattr(w.app, "debug") and w.app.debug:
            p.fillRect(QRectF(s.ew, s.eh, s.w, s.h), QColor(0, 100, 0, 100))
            p.fillRect(QRectF(0, 0, s.w, s.h), QColor(255, 0, 255, 100))
        if s.animated:
            fr = s.frame
            if isinstance(gfx, list) or isinstance(gfx, tuple):
                gfx = gfx[s.frame]
                s.frame = 0
            p.drawImage(0, 0, gfx, s.sx + s.frame * (s.w + s.ew), s.sy, s.w + s.ew, s.h + s.eh)
            s.frame = fr
        else:
            p.drawImage(0, 0, gfx, s.sx, s.sy, s.w + s.ew, s.h + s.eh)

    def paintSprites(w, p, l, paintTexts = False):
        for s in l.sprites:
            if isinstance(s, Text):
                if paintTexts:
                    w.paintText(p, s)
            else:
                p.save()
                p.translate(round(s.x), round(s.y))
                p.translate(s.w / 2, s.h / 2)
                p.rotate(s.r)
                p.scale(s.z * s.zx, s.z * s.zy)
                p.translate(-s.w / 2, -s.h / 2)
                if isinstance(s, Group):
                    w.paintSprites(p, s, True)
                else:
                    w.paintSprite(p, s)
                p.restore()

    def paintText(w, p, s):
        if hasattr(s, "color"):
            p.setPen(makeqcolor(s.color))
        else:
            p.setPen(w.fgColor())
        font = p.font()
        font.setPixelSize(int(s.size))
        p.setFont(font)
        rect = QRectF(s.x, s.y, s.w, s.h)
        if s == w.app.top:
            align = Qt.AlignmentFlag.AlignTop
            rect = rect.adjusted(0, 0, 0, 8000)
        elif s == w.app.bot:
            align = Qt.AlignmentFlag.AlignBottom
            rect = rect.adjusted(0, -8000, 0, 0)
        else:
            align = Qt.AlignmentFlag.AlignVCenter
            rect = rect.adjusted(0, -8000, 0, 8000)
        if s.text != '':
            if hasattr(s, "html") and s.html:
                ctx = QAbstractTextDocumentLayout.PaintContext()
                ctx.palette.setColor(QPalette.Text, p.pen().color())
                td = QTextDocument()
                if s.w > 0:
                    td.setTextWidth(s.w)
                td.setHtml(s.text)
                p.save()
                p.translate(rect.center())
                p.translate(-td.size().width() / 2, -td.size().height() / 2)
                td.documentLayout().draw(p, ctx)
#                td.drawContents(p);
                p.restore()
            else:
                p.drawText(rect.adjusted(-8000, 0, 8000, 0), align | Qt.AlignmentFlag.AlignHCenter, s.text)
        if s.left != '':
            p.drawText(rect.adjusted(0, 0, 8000, 0), align | Qt.AlignmentFlag.AlignLeft, s.left)
        if s.right != '':
            p.drawText(rect.adjusted(-8000, 0, 0, 0), align | Qt.AlignmentFlag.AlignRight, s.right)

    def paintTexts(w, p):
        w.app.centertext.text = w.app.text if w.timer != None else w.app.text + "\n(Paused)"
        for s in w.sprites + [ w.app.top, w.app.bot, w.app.centertext ]:
            if not isinstance(s, Text):
                continue
            if s.text == '' and s.left == '' and s.right == '':
                continue
            p.save()
            p.translate(s.x + s.w / 2, s.y + s.h / 2)
            p.rotate(s.r)
            p.scale(s.z * s.zx, s.z * s.zy)
            p.translate(-(s.x + s.w / 2), -(s.y + s.h / 2))
            w.paintText(p, s)
            p.restore()

    def paintEvent(w, e):
        p = QPainter(w)
        p.scale(w.scale, w.scale)
        w.paintBackground(p)
        w.paintSprites(p, w)
#        w.paintForeground(p)
        w.paintTexts(p)

    def timerEvent(w, e):
        paint = False
        f = 60 * w.app.appspeed / w.app.fps
        for s in w.sprites:
            if s.animated and s.frames > 0 and s.fps > 0:
                s.ticks += 1
                ticksPerFrame = int(w.app.fps / s.fps + 0.5)
                if ticksPerFrame < 1:
                    ticksPerFrame = 1
                s.ticks %= ticksPerFrame
                if not s.ticks:
                    s.frame += 1
                    s.frame %= s.frames
                    paint = True
            if s.vx or s.vy:
                s.x += s.vx * f
                s.y += s.vy * f
                paint = True
            s.vx += s.ax * f
            s.vy += s.ay * f
        if hasattr(w.app, "frame"):
            pos = w.mapFromGlobal(QCursor.pos()) / w.scale
            w.app.mouse.x = pos.x()
            w.app.mouse.y = pos.y()
            w.app.time = w.frame * w.app.appspeed / w.app.fps
            result = w.app.frame()
            if not hasattr(w, "always_update") or w.always_update:
                result = True
            paint = result
        if paint:
            w.update()
        w.frame += 1


##############################################################################
#
#  Form
#

class Form(QDialog):
    def __init__(self, title = '', parent = None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(title)
        self.form = QFormLayout()
        hboxlayout = QVBoxLayout(self)
        hboxlayout.addLayout(self.form)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButtons.Ok | QDialogButtonBox.StandardButtons.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        hboxlayout.addWidget(buttons)
        self.gotFocus = False

    def addRow(self, label, widget):
        self.form.addRow(label, widget)
        if not self.gotFocus and widget.focusPolicy != 0:
            widget.setFocus()
            self.gotFocus = True

    def input_str(self, label, default = ''):
        widget = QLineEdit()
        widget.setText(default)
        self.addRow(label, widget)

    def input(self, label):
        self.input_str(label)

    def input_text(self, label, default = ''):
        widget = QPlainTextEdit()
        widget.setPlainText(default)
        self.addRow(label, widget)

    def input_int(self, label, default = 0, maxval = 2**31 - 1, minval = 0):
        widget = QSpinBox()
        widget.setRange(minval, maxval)
        widget.setValue(default)
        self.addRow(label, widget)

    def input_float(self, label, default = 0.0):
        widget = QDoubleSpinBox()
        widget.setValue(default)
        self.addRow(label, widget)

    def choice(self, label, default = False):
        if isinstance(default, list):
            widget = QComboBox()
            widget.addItems(default)
        else:
            widget = QRadioButton()
            widget.setChecked(default)
        self.form.addRow(label, widget)

    def input_bool(self, label, default = False):
        widget = QCheckBox()
        widget.setChecked(default)
        self.form.addRow(label, widget)

    def separator(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.HLine)
        self.form.addRow(" ", frame)

    def caption(self, label):
        widget = QLabel(label)
        font = self.font()
        font.setBold(True)
        widget.setFont(font)
        self.form.addRow(" ", widget)

    def _setVar(self, name, widget):
        if name[-1] == ':':
            name = name[:-1]
#        print(name, widget)
        if hasattr(widget, "isChecked"):
            setattr(self, name, widget.isChecked())
        elif hasattr(widget, "value"):
            setattr(self, name, widget.value())
        elif hasattr(widget, "toPlainText"):
            setattr(self, name, widget.toPlainText())
        elif hasattr(widget, "currentText"):
            setattr(self, name, widget.currentText())
        elif isinstance(widget, QFrame) or isinstance(widget, QLabel):
            pass
        elif hasattr(widget, "text"):
            setattr(self, name, widget.text())
        else:
            print("No widget attribute found for", name)

    def setVars(self):
        for row in range(self.form.count() // 2):
            label = self.form.itemAt(2 * row + 0)
            widget = self.form.itemAt(2 * row + 1).widget()
            name = label.widget().text()
            self._setVar(name, widget)

    def ok(self):
        self.setVars()
        return self.result() == QDialog.Accepted


##############################################################################
#
#  App
#

class App(QApplication):
    fps = 60
    time = 0
    appspeed = 1

    def __init__(app, name = ''):
        if name == '':
            name = app.__class__.__name__
        QApplication.__init__(app, [name])
        app.settings = QSettings("de.maxiom.AppEngine", name)
        app.sprites = []
        app.key = 0
        app.kx = 0
        app.ky = 0
        app.centertext = Text()
        app.window = Window()
        app.window.app = app
        app.size = QSize(640, 480)
        app.resized()
        app.mouse = Area(1, 1)
        app.text = ''
        app.background = QApplication.palette().window().color()
        app.centertext.size = 40

    def setBackground(app, gfx):
        app.window.bg = makeqimage(gfx)
        app.size = app.window.bg.size()
        app.resized()

    def resized(app):
        h = app.primaryScreen().geometry().height()
        if hasattr(app, "scale"):
            app.window.scale = app.scale
        else:
            app.window.scale = int((h - 120) / 480 * 4) / 4
#        print(app.window.scale)
#        app.window.scale = 1
        app.window.setFixedSize(app.size * app.window.scale)
        app.w = app.size.width()
        app.h = app.size.height()
        app.area = Area(app.w, app.h)
        app.centertext.center_in(app.area)
        app.top = Text(app.w - 30, 20)
        app.top.x = 15
        app.top.y = 5
        app.top.size = 20
        app.bot = Text(app.w - 30, 20)
        app.bot.x = 15
        app.bot.y = app.h - 25
        app.bot.size = 20
        app.output = app.top

    def setSpriteSheet(app, gfx):
        app.window.fg = makeqimage(gfx)

    def exec(app, fullscreen = False):
        globals()["appwindow"] = app.window
        if fullscreen:
            app.window.showFullScreen()
        else:
            app.window.show()
        if hasattr(QApplication, "_exec"):
            return QApplication._exec()
        return QApplication.exec()

    def showMouseCursor(app):
        app.window.setCursor(Qt.CursorShape.ArrowCursor)

    def hideMouseCursor(app):
        app.window.setCursor(Qt.CursorShape.BlankCursor)

    def setCursorShape(app, s = "arrow"):
        if s != "blank":
            app.showMouseCursor()
        else:
            app.hideMouseCursor()

    def show(app, s):
        if s is app.mouse:
            app.showMouseCursor()
            return
        if isinstance(s, list):
            for i in s:
                app.show(i)
            return
        if s in app.window.sprites:
            app.window.sprites.remove(s)
        app.window.sprites.append(s)

    def hide(app, s):
        if s is app.mouse:
            app.hideMouseCursor()
            return
        if isinstance(s, list):
            for i in s:
                app.hide(i)
            return
        if s in app.window.sprites:
            app.window.sprites.remove(s)
            s.pressed = 0

    def input(app, prompt):
        return QInputDialog.getText(app.window, "Input", prompt)[0]

    def print(app, text):
        if app.output is app.top or app.output is app.bot:
            (app.output).left += text + "\n"
        else:
            (app.output).text += text + "\n"

    def timer(app):
        return Timer(app)


class Timer:
    def __init__(t, app):
        t.app = app
        t.start()

    def start(t):
        t.starttime = t.app.time

    def time(t):
        return t.app.time - t.starttime

    def seconds(t):
        return int(t.time())

    def minutes(t):
        s = t.seconds()
        m = s // 60
        s -= m * 60
        return str(m) + ":" + str(s).zfill(2)


class Game(App):
    def __init__(app, name = ''):
        App.__init__(app, name)
        app.background = QColor(0, 0, 0)


##############################################################################
#
#  main
#

# Exceptions (Fehlerausnahmen) abfangen
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    if "appwindow" in globals():
        appwindow.close()

sys.excepthook = except_hook

_ = None

if __name__ == "__main__":
    app = App("About engine.py")
    app.size = QSize(320, 160)
    app.resized()
    app.background = RGB(200, 220, 240)
    bg = Graphics((app.w, app.h))
    bg.execShader(lambda x, y, uniform: qRgb(200 - y // 5, 220 - y // 5, 240 - y // 5))
    bg.execPainter(lambda p, uniform: (p.drawLine(0, 126, 320, 126), p.drawLine(0, 36, 320, 36)))
    app.setBackground(bg)
    bug = Sprite(32, 32)
    bug.setGraphics(Emoji('mosquito'))
    bug.z = 0.5
    bug.x = 90000
    bug.y = 40000
    bug.r = 30
    app.show(bug)
    app.top.text = Emoji('rocket').text + " " + MODULE_NAME + " " + MODULE_VERSION
    app.centertext.size = 14
    app.output = app
    app.print(MODULE_COPYRIGHT)
    app.print("License: " + MODULE_LICENSE)
    app.print(MODULE_MAIL.replace('/', Emoji('lollipop').text))
    app.print(MODULE_URL)
    app.text = app.text[:-1]
    app.bot.text = "Please report bugs!"
    app.window.keyPressEvent = lambda event: app.quit() # disable Pause key
    app.frame = lambda: (bug.moveTo(random.randrange(300), random.randrange(140), 0.5), app.quit() if app.mouse.pressed else False)[-1]
    app.exec()

