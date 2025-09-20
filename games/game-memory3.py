from engine import *


def random_place(o):
    x = random.randrange(6)
    y = random.randrange(5)
    if texts[x,y] == None:
        texts[x,y] = o
    else:
        random_place(o)


def start():
    for x,y in cover:
        if cover[x,y].pressed:
            app.needed.start()
            app.frame = frame


def checkpair():
    if len(app.guess) == 3:
        g0 = app.guess[0]
        g1 = app.guess[1]
        g2 = app.guess[2]
        if texts[g0[0],g0[1]] == texts[g1[0],g1[1]] and texts[g0[0],g0[1]] == texts[g2[0],g2[1]]:
            for g in app.guess:
#                app.hide(bg[g[0],g[1]])
#                app.hide(board[g[0],g[1]])
                board[g[0],g[1]].transparency = 0.5
                bg[g[0],g[1]].transparency = 0.5
            app.guess = []
        else:
            app.delay.start()


def process_input():
    for x,y in cover:
        if cover[x,y].pressed:
            app.hide(cover[x,y])
            app.guess.append([x,y])
            checkpair()


def frame():
    checkdone()
    app.top.right = app.needed.minutes()
    if len(app.guess) > 0:
        app.top.text = str(len(app.guess))
    else:
        app.top.text = ''
    if len(app.guess) == 3:
        if app.delay.time() > 0.75:
            for g in app.guess:
                app.show(cover[g[0],g[1]])
            app.guess = []
    else:
        process_input()


def checkdone():
    for x,y in board:
        if board[x,y].transparency != 0.5:
            return
    app.frame = game_over


def game_over():
    app.top.text = "GAME OVER"


app = App("Memory³")

app.background = (120, 70, 0)
app.top.text = "MEMORY³"

app.needed = app.timer()
app.delay = app.timer()

app.guess = []

bgname = 'white large square'
#bgname = 'black large square'
covers = [0x1F301, 0x1F303, 0x1F304, 0x1F305, 0x1F306, 0x1F307, 0x1F309, 0x1F30C,
          0x1F320, 0x1F386, 0x1F387, 0x1F391, 0x1F3D9, 0x1F3DC, 0x1F3DE]
covername = covers[random.randrange(len(covers))]

level = 1

if level == 1:
    pictures = ["house building", "oncoming police car", "ball of yarn", "father christmas", "jack-o-lantern", "green book",
            "princess", "drum with drumsticks", "top hat", "bucket" ]
elif level == 2:
    pictures = ["optical disc", "floppy disk", "videocassette", "fax machine", "alarm clock",
                "radio", "camera with flash", "clipboard", "abacus", "books"]
elif level == 3:
    pictures = ["dog face", "pig face", "frog face", "hamster face", "wolf face",
               "bear face", "panda face", "tiger face", "cat face", "monkey face"]
elif level == 4:
    pictures = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
elif level == 5:
    pictures = ["large red square", "large green square", "large blue square", "large yellow square", "large purple square",
               "large red circle", "large green circle", "large blue circle", "large yellow circle", "large purple circle"]
elif level == 6:
    pictures = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    '''
    u = random.randint(0x1F42D, 0x1F43C - 9)
    for n in range(u, u + 10):
        pictures.append(n)
    '''
else:
    pictures = ["cat face"]
    for n in range(0x1F638, 0x1F638 + 9):
        pictures.append(n)
    '''
    pictures = []
    u = random.randint(0x1F600, 0x1F637 - 9)
    for n in range(u, u + 10):
        pictures.append(n)
    '''

bg = Grid(6, 5)

s = Emoji(bgname, 80)
bg_gfx = s.graphics()

s = Emoji(covername, 80)
cover_gfx = s.graphics()

for x,y in bg:
    s = Sprite(80, 80)
    s.setGraphics(bg_gfx)
    s.x = 80 + 80 * x
    s.y = 40 + 80 * y
    bg[x,y] = s
    app.show(s)

texts = Grid(6, 5)

for o in pictures:
    random_place(o)
    random_place(o)
    random_place(o)

board = Grid(6, 5)

for x,y in board:
    s = Emoji(texts[x,y], 60)
    gfx = s.graphics()
    s = Sprite(s.w, s.h)
    s.setGraphics(gfx)
    s.transparency = 0
    s.x = 90 + 80 * x
    s.y = 50 + 80 * y
    board[x,y] = s
    app.show(s)

cover = Grid(6, 5)

for x,y in cover:
    s = Sprite(80, 80)
    s.setGraphics(cover_gfx)
    s.x = 80 + 80 * x
    s.y = 40 + 80 * y
    cover[x,y] = s
    app.show(s)

app.frame = start
app.exec()

