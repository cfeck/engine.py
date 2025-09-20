from engine import *
from random import randint


def start():
    ping_player.y = 300
    ping_player.color = RGB(200, 200, 200)
    pong_player.y = 200
    pong_player.color = RGB(255, 255, 255)
    ball.x = 20
    ball.y = 340
    shadow.x = 20
    shadow.y = 345
    app.text = "  PING PONG "
    app.bot.text = "Press Up/Down to Start"
    if app.key and app.ky:
        app.last_move = -5
        app.last_time = app.time
        app.text = ""
        app.bot.text = ""
        app.player = pong_player
        impact3.play()
        ball.vx = 10
        ball.vy = randint(-6, -2)
        ball.ax = -0.08
        app.hide(app.mouse)
        app.score = 0
        app.frame = ping


def ai_player():
    if app.time > app.last_time + 0.1:
        if ball.y > app.player.y + 60:
            app.last_move = 5
            app.last_time = app.time
        elif ball.y < app.player.y + 20:
            app.last_move = -5
            app.last_time = app.time
    app.player.vy = app.last_move
    app.player.keep_in(app.area)


def handle_input():
    app.player.vy = 5 * app.ky
    app.player.keep_in(app.area)


def ball_reflect():
    if ball.y <= 0:
        ball.vy = abs(ball.vy)
        impact4.play()
    if ball.y >= 460:
        ball.vy = -abs(ball.vy)
        impact4.play()
    shadow.x = ball.x
    shadow.y = ball.y + 35 - ((ball.x - 310) ** 2) // 3000


def ping():
    ai_player()
#    handle_input()
    ball_reflect()
    if ball.hits(app.player):
        ball.vy = -(app.player.y + 30 + randint(0,20) - ball.y) // 8
        ball.vx = -10
        ball.ax = 0.08
        app.frame = pong
        app.player.vy = 0
        app.player.color = RGB(200, 200, 200)
        app.player = ping_player
        app.player.color = RGB(255, 255, 255)
        impact3.play()
        app.score += 1
        app.top.text = str(app.score)
    elif ball.x >= 620:
        app.frame = game_over
        app.left_score += app.score
        app.score = 0
        app.top.left = "Score: " + str(app.left_score)
        app.top.text = ''
        shutdown1.play()


def pong():
    handle_input()
    ball_reflect()
    if ball.hits(app.player):
        ball.vy = -(app.player.y + 30 + randint(0,20) - ball.y) // 8
        ball.vx = 10
        ball.ax = -0.08
        app.frame = ping
        app.player.vy = 0
        app.player.color = RGB(200, 200, 200)
        app.player = pong_player
        app.player.color = RGB(255, 255, 255)
        app.last_time = app.time
        impact3.play()
        app.score += 1
        app.top.text = str(app.score)
    elif ball.x <= 0:
        app.frame = game_over
        app.right_score += app.score
        app.score = 0
        app.top.right = "Score: " + str(app.right_score)
        app.top.text = ''
        shutdown1.play()


def game_over():
    ping_player.vy = 0
    pong_player.vy = 0
    app.text = "GAME OVER "
    app.hide(ball)
    app.hide(shadow)
    app.show(app.mouse)


def noiseShader(x, y, uniform):
    color = uniform[0]
    variance = uniform[1]
    r = color.R() + randint(-variance, +variance)
    g = color.G() + randint(-variance, +variance)
    b = color.B() + randint(-variance, +variance)
    return qRgba(r, g, b, 255)


app = App("Ping Pong")

impact3 = Sound("sfx_sounds_impact3.wav")
impact4 = Sound("sfx_sounds_impact4.wav")
shutdown1 = Sound("sfx_sound_shutdown1.wav")

#app.background = RGB(160, 80, 40) # Sand
app.background = RGB(40, 80, 20) # Grass
#app.background = RGB(40, 80, 150) # Blue
bg = Graphics((640, 480))
bg.execShader(noiseShader, app.background, 15)
app.setBackground(bg)

net = Sprite(4, 420)
net.color = RGB(200, 200, 200)
net.center_in(app.area)
app.show(net)

shadow = Sprite(20, 20)
shadow.corner_radius = 10
shadow.transparency = 0.8
shadow.color = RGB(0, 0, 0)
app.show(shadow)

ball = Sprite(20, 20)
ball.color = RGB(210, 250, 80)
ball.corner_radius = 10
#ball.setGraphics(Emoji('softball', 20).graphics())
#ball = Emoji('softball', 20)
app.show(ball)

ping_player = Sprite(20, 100)
ping_player.corner_radius = -1
app.show(ping_player)

pong_player = Sprite(20, 100)
pong_player.corner_radius = -1
pong_player.x = 620
app.show(pong_player)

app.left_score = 0
app.right_score = 0

app.frame = start
app.exec()

