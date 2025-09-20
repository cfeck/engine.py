from engine import *
from random import randint

def play():
    game.top.right = "Lifes: " + str(game.lifes)
    game.top.left = "Coins: " + str(game.coins)

    for tile in tiles:
        y = 400 - player.y
        if y < 0:
            y = 0
        if y > 640:
            y = 640
#        y = 0
        tile.y = tile.ty - y / 20
        if tile.x > 640:
            tile.x -= 1280

    if dust.frame == 8:
        game.hide(dust)
        player.hit = False

    if game.lifes == 0:
        game.text = "GAME OVER"
        game.hide(player)
        game.hide(coin)
        for tile in tiles:
            tile.vx *= 0.99
            if tile.vx < 0.25:
                tile.vx = 0
#            tile.setSheetPos(768, tile.sy)
        for wall in walls:
            wall.vx *= 0.99
            if wall.vx < 0.25:
                wall.vx = 0
#            wall.setSheetPos(512 - 4 * 64, 256 + 2 * 64)
        return

    if game.key or game.mouse.pressed:
        r = randint(1, 2)
        player.setSheetPos(512 - r * 64, 256 - 24 - r * 4)
        player.vy = -5
        player.vx = -(player.x - 400) / 200
    else:
        if player.y > 400: # or player.y < 0 or player.vy > 8:
            player.setSheetPos(512 + 64, 256)
        else:
            player.setSheetPos(512, 256 - 12)
        player.vx = -(player.x - 580) / 100
    if player.y > 480 - 60:
        player.y = 480 - 60
#    if player.y < 0:
#        player.y = 0

    if player.hits(coin) and not coin.hit:
        coin.frame = 4
        coin.frames = 9
        coin.hit = True
        game.coins += 1
        if game.coins % 10 == 0:
            game.lifes += 1

    if coin.x > 640 or coin.frame == 8:
        coin.x = randint(-2000, -200)
        coin.y = randint(-40, 456)
        coin.hit = False
        coin.frames = 4
        coin.frame = 0

    wy = randint(100, 500)
    if wy < 300:
        wy -= 500
    else:
        wy -= 130
    for wall in walls:
        if player.hits(wall) and not player.hit:
            dust.x = player.x
            dust.y = player.y
            dust.frame = 0
            game.show(dust)
            player.hit = True
            if player.y > 240:
                player.y = -40
            else:
                player.y = 400
            player.x = 512
            player.vy = -2
            game.lifes -= 1
            if game.lifes == 0:
                player.x = -1000
        if wall.x > 640:
            wall.x -= game.walldist * 4
            wall.y = wall.ty + wy
#        wall.vx = 6 - (game.walldist - 230) / 100

    if game.walldist > 210:
        game.walldist -= 0.02


game = App("Rockato")
game.background = "black"
game.frame = play
game.setCursorShape("blank")
# game.debug = True

game.setSpriteSheet("arcade_platformerV2-fixedx4.png")

game.lifes = 3
game.coins = 0

game.walldist = 600

tiles = []
for tx in range(2):
    if True:
        for ty in range(5):
            tile = Sprite(640, 128)
            tile.setSheetPos(0, 640 + ty * 128)
            tile.x = tx * 640
            tile.ty = ty * 128 - 64
            tile.vx = ty * 0.5
            game.show(tile)
            tiles.append(tile)
    else:
        tile = Sprite(640, 640)
        tile.setSheetPos(0, 640)
        tile.x = tx * 640
        tile.ty = -64
        tile.vx = 1
        game.show(tile)
        tiles.append(tile)

walls = []
for tx in range(4):
    for ty in range(8):
        wall = Sprite(64, 64)
        wall.setSheetPos(0, 256 + 3 * 64)
        wall.x = (tx - 3) * game.walldist
        wall.ty = ty * 64
        wall.vx = 2
        wall.y = wall.ty + 420 - (3 - tx) * 50
        game.show(wall)
        walls.append(wall)

player = Sprite(64, 64)
player.setSheetPos(512, 256 - 12)
player.hit = False
player.x = 512
player.y = 240
player.ay = 0.25
player.eh = 20
player.vy = -10
game.show(player)

coin = Animation(64, 64)
coin.setSheetPos(512 - 64 * 4, 256 + 3 * 64)
coin.hit = False
coin.x = -2100
coin.y = 200
coin.vx = 3
coin.frames = 4
coin.fps = 10
game.show(coin)

dust = Animation(64, 64)
dust.setSheetPos(0, 256 + 4 * 64)
dust.fps = 10
dust.frames = 9

game.centertext.color = "black"

game.exec()

