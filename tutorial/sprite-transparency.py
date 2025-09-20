from engine import Game, Sprite


game = Game()

block1 = Sprite(200, 200)
block1.transparency = 0.25
block1.x = 200
block1.y = 100

block2 = Sprite(200, 200)
block2.transparency = 0.75
block2.x = 300
block2.y = 200

game.show(block1)
game.show(block2)

game.exec()

