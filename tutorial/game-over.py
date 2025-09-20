from engine import Game, Sprite


def frame():
    if player.hits(block):
        game.frame = game_over


def game_over():
    player.vx = 0
    game.text = "GAME OVER"


game = Game()

player = Sprite(40, 40)
player.vx = 2
player.y = 30
game.show(player)

block = Sprite(100, 100)
block.x = 500
game.show(block)

game.frame = frame
game.exec()

