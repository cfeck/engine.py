from engine import *


def turn_player1():
    cell = board[1,1]
    if cell.text == '':
        cell.text = "🐭🐱"[game.turn]
        cell.size_v = 10 + 10 * game.turn
        game.turn = 0
    for x,y in board:
        cell = board[x,y]
        if cell.text == '' and game.turn == 1:
            cell.text = "🐭🐱"[game.turn]
            cell.size_v = 10 + 10 * game.turn
            game.turn = 0


def turn_player2():
    for x,y in board:
        cell = board[x,y]
        if cell.hits(game.mouse):
            if cell.text == '' and game.turn == 0:
                cell.text = "🐭🐱"[game.turn]
                cell.size_v = 10 + 10 * game.turn
                game.turn = 1


def row_winner(x, y, dx, dy):
    winner = board[x,y].text
    if winner == '':
        return
    for i in range(2):
        x += dx
        y += dy
        if board[x,y].text != winner:
            return
    return winner


def winner():
    winning_rows = [ (0, 0, 1, 0), (0, 1, 1, 0), (0, 2, 1, 0),
                     (0, 0, 0, 1), (1, 0, 0, 1), (2, 0, 0, 1),
                     (0, 0, 1, 1), (0, 2, 1, -1) ]
    for r in winning_rows:
        winner = row_winner(r[0], r[1], r[2], r[3])
        if winner:
            return winner
    return


def frame():
    finished = True
    if not winner():
        for x,y in board:
            cell = board[x,y]
            if cell.text == "":
                finished = False

    if finished:
        game.top.text = "GAME OVER, winner is " + str(winner())
    else:
        if game.turn == 1 and not game.mouse.pressed:
            turn_player1()
        if game.turn == 0 and game.mouse.pressed:
            turn_player2()
    animate_cells()


def animate_cells():
    for x,y in board:
        cell = board[x,y]
        cell.size += cell.size_v
        cell.size_v += cell.size_a
        cell.size_a = -0.5 * (cell.size - 80.5)
        cell.size_v = 0.5 * cell.size_v
        cell.r = cell.size - 80


game = App("Tic-Tac-Toe")

game.background = RGB(40, 80, 20)

game.turn = 1

board = Grid(3, 3)

for x,y in board:
    cell = Text()
    cell.w = 80
    cell.h = 80
    cell.x = (x - 1) * 100 + 200
    cell.y = (y - 1) * 100 + 200
    cell.size = 80
    cell.text = ''
    cell.color = "skyblue"
    cell.size_v = 0
    cell.size_a = 0
    board[x,y] = cell
    game.show(cell)

for n in range(4):
    line = Sprite(300, 2)
    line.x = 90
    line.y = 90 + 100 * n
    game.show(line)

    line = Sprite(2, 300)
    line.x = 90 + 100 * n
    line.y = 90
    game.show(line)

game.frame = frame
game.exec()

