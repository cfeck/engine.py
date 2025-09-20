from engine import *
from random import randint


class Scroller(Game):
    def frame(game):
        if game.key:
            game.show(ball)
        else:
            game.hide(ball)
#        if game.key:
#        ball.vx = 2 * game.kx
#        ball.vy = 2 * game.ky
#        ball.ax = 0.05 * game.kx
#        ball.ay = 0.05 * game.ky
#        else:
#            ball.vx = 0
#            ball.vy = 0
        for tile in tiles:
            tile.x -= 1 * game.kx
            if tile.x < -80:
                tile.x += 720
            if tile.x > 640:
                tile.x -= 720
            tile.y -= 1 * game.ky
            if tile.y < -80:
                tile.y += 560
            if tile.y > 480:
                tile.y -= 560

        for wall in walls:
            wall.x -= 2 * game.kx
            if wall.x < -80:
                wall.x += 720
            if wall.x > 640:
                wall.x -= 720
#        ball.x -= 1
#        ball.y -= 1


game = Scroller()
game.setCursorShape("blank")
bg = Graphics("breakout_bg.png")
#game.setBackground(bg)
#game.setBackground("breakout_bg.png")
sprites = Graphics("breakout_sprites_fixed.png")
game.setSpriteSheet(sprites)

tiles = []
for xt in range(9):
    for yt in range(7):
        tile = Sprite(80, 80)
        tile.x = xt * tile.w
        tile.y = yt * tile.h
        tile.setGraphics(bg)
        tile.setSheetPos(200, 0)
        tiles.append(tile)
        game.show(tile)

walls = []
for xt in range(9):
    wall = Sprite(80, 80)
    wall.setGraphics(bg)
    wall.setSheetPos(80, 400)
    wall.x = xt * wall.w
    wall.y = 280
    walls.append(wall)
    game.show(wall)

ball = Sprite(24, 24)
ball.setSheetPos(40 * 4, 40 * 6)
ball.x = game.w / 2 - ball.w / 2
ball.y = game.h / 2 - ball.h / 2
game.show(ball)

text = Text()
text.text = "Game Over"
#text.color = "red"
#text.size = 40
text.x = 200
text.y = 200
game.show(text)

game.kx = 1

game.exec()


