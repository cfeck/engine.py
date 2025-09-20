from engine import *

class TestGame(Game):
    def frame(game):
        game.text = str(game.kx) + "," + str(game.ky) + " " + str(game.key)
        for x,y in grid:
            grid[x,y].x += 1


game = TestGame()

grid = Grid(10, 8)
for x,y in grid:
    player = Text()
    player.text = chr(128512 + 10 * y + x)
    player.x = 20 * x + 20
    player.y = 20 * y + 20
    grid[x,y] = player
    game.show(player)

game.exec()

