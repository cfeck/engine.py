from engine import *


class Block(Sprite):
    def __init__(b, x, y):
        Sprite.__init__(b, 32, 32)
        b.setSheetPos(40 * x, 40 * y)
        b.setShadow(8)


def start():
    game.text = "Click Ball>       to Start"
    if game.mouse.pressed and game.mouse.hits(ball):
        game.starttime = game.time
        game.text = ""
        game.frame = play


def play():
    update_time()
    ball_move()
    ball_test_walls()
    if ball_hits_any_block():
        if not game.gotblock and len(blocks) < 10:
            new_block()
            game.gotblock = True
    else:
        game.gotblock = False
    if ball.hits(target):
        ball_hit_target()


def update_time():
    seconds = int(game.time - game.starttime)
    minutes = seconds // 60
    seconds -= 60 * minutes
    time.text = "Time\n" + str(minutes) + ":" + str(seconds).zfill(2)


def update_remaining():
    remaining.text = "Blocks\n" + str(len(blocks))
    for block in blocks:
        if len(blocks) < 10:
            block.setSheetPos(0, 0)
        else:
            block.setSheetPos(40 * 2, 0)

def ball_move():
    ball.ax = 0.003 * (game.mouse.x - game.w / 2)
    ball.ay = 0.003 * (game.mouse.y - game.h / 2)

    ball.vx *= 0.99
    ball.vy *= 0.99


def ball_test_walls():
    if ball.x < 80 or ball.x > game.w - 80 - ball.w:
        ball.x -= ball.vx
        ball.vx = -0.5 * ball.vx
        ball.ax *= 0.9

    if ball.y < 0 or ball.y > game.h - 0 - ball.w:
        ball.y -= ball.vy
        ball.vy = -0.5 * ball.vy
        ball.ay *= 0.9


def ball_hits_any_block():
    for block in blocks:
        if ball.hits(block):
            return True
    return False


def new_block():
    if len(blocks) < 10:
        block = Block(0, 0)
    else:
        block = Block(2, 0)
    block.random_in(game.area)
    blocks.append(block)
    game.show(block)
    update_remaining()
    game.show(target)
    game.show(ball)


def ball_hit_target():
    target.random_in(game.area)
    block = blocks[0]
    game.hide(block)
    blocks.remove(block)
    update_remaining()
    if len(blocks) == 0:
        game.timeneeded = round(game.time - game.starttime)
        game.frame = end


def end():
    game.text = "Game Over"
    game.hide(target)
    game.hide(ball)
    game.hide(center)


game = App("Tilt")

bg = Graphics("breakout_bg.png")
game.background = RGB(20, 25, 30)
game.setSpriteSheet("breakout_sprites_fixed.png")

game.area = Area(480, 480)
game.area.x = 80
game.area.y = 0

'''
for xt in range(8):
    for yt in range(6):
        tile = Sprite(80, 80)
        tile.x = xt * tile.w
        tile.y = yt * tile.h
        tile.setGraphics(bg)
        tile.setSheetPos(200, 0)
        game.show(tile)
'''

for yt in range(6):
    tile = Sprite(80, 80)
    tile.x = 0
    tile.y = yt * tile.h
    tile.setGraphics(bg)
    tile.setSheetPos(80, 0)
    game.show(tile)

    tile = Sprite(80, 80)
    tile.x = game.w - tile.w
    tile.y = yt * tile.h
    tile.setGraphics(bg)
    tile.setSheetPos(80, 0)
    game.show(tile)

game.gotblock = False

blocks = []

for i in range(20):
    block = Block(2, 0)
    block.random_in(game.area)
    blocks.append(block)
    game.show(block)

target = Block(6, 0)
target.random_in(game.area)
game.show(target)

center = Sprite(16, 16)
center.center_in(game.area)
center.setSheetPos(40 * 4, 40 * 5)
game.show(center)

ball = Sprite(24, 24)
ball.setSheetPos(40 * 4, 40 * 6)
ball.center_in(game.area)
game.show(ball)

time = Text()
time.x = 600
time.y = 40
game.show(time)

remaining = Text()
remaining.x = 40
remaining.y = 40
game.show(remaining)

game.frame = start
game.exec()

