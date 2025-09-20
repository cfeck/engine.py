from engine import *


def rechts():
    player.y += 10
    if player.y == 480:
        player.seite = unten

def unten():
    player.x += 10
    if player.x == 640:
        player.seite = links

def links():
    player.y -= 10
    if player.y == 0:
        player.seite = oben

def oben():
    player.x -= 10
    if player.x == 0:
        player.seite = rechts

def frame():
    player.seite()
    game.text = "(" + str(player.x) + "|" + str(player.y) + ")"


game = Game()

#game.fps = 5

#player = Sprite(20, 20)
player = Text()
#player = Text(50, 50)
player.seite = rechts
player.text = chr(128512)
#player.text = "X"
#player.size = 50
#player.color = "red"

game.frame = frame
game.show(player)

game.exec()

'''
def animate(player):
    if player.seite == "rechts":
        player.y += 2
        if player.y == 100:
            player.seite = "unten"
    if player.seite == "unten":
        player.x += 2
        if player.x == 100:
            player.seite = "links"
    if player.seite == "links":
        player.y -= 2
        if player.y == 0:
            player.seite = "oben"
    if player.seite == "oben":
        player.x -= 2
        if player.x == 0:
            player.seite = "rechts"


class TestGame(Game):
    def frame(game):
        animate(player)

#        game.text = "(" + str(player.x) + "|" + str(player.y) + ")"

#        game.text = str(game.window.frame)

game = TestGame()

#game.fps = 5

#player = Sprite(20, 20)
player = Text()
#player = Text(50, 50)
player.seite = "rechts"
player.text = chr(128512)
#player.text = "X"
#player.size = 50
#player.color = "red"

game.show(player)

game.exec()

'''
