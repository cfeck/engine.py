from engine import Game, Emoji


def ping():
    sprite.zx = 1
    sprite.r = 50
    sprite.x += 5
    if sprite.x > 560:
        game.frame = pong


def pong():
    sprite.zx = -1
    sprite.r = -50
    sprite.x -= 5
    if sprite.x < 0:
        game.frame = ping


game = Game()

game.background = "skyblue"

sprite = Emoji("superhero", 80)
sprite.center_in(game.area)
game.show(sprite)

game.frame = ping
game.exec()

