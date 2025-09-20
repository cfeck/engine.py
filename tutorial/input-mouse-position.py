from engine import *


def frame():
    for sprite in [ player, t, b, l, r]:
        sprite.center_in(game.mouse)

    t.y = 0
    b.y = 460
    l.x = 0
    r.x = 620


game = Game()

player = Sprite(40, 40)
game.show(player)

t = Sprite(100, 20)
b = Sprite(100, 20)
l = Sprite(20, 100)
r = Sprite(20, 100)
game.show(t)
game.show(b)
game.show(l)
game.show(r)

game.frame = frame
game.exec()

