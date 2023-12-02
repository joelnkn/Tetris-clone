import numpy

PIECE_I = [
    [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],

    [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
    ],

    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
    ],

    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ],
]

PIECE_J = [
    [
        [2, 0, 0],
        [2, 2, 2],
        [0, 0, 0],
    ],

    [
        [0, 2, 2],
        [0, 2, 0],
        [0, 2, 0],
    ],

    [
        [0, 0, 0],
        [2, 2, 2],
        [0, 0, 2],
    ],

    [
        [0, 2, 0],
        [0, 2, 0],
        [2, 2, 0],
    ],
]

PIECE_L = [
    [
        [0, 0, 3],
        [3, 3, 3],
        [0, 0, 0],
    ],

    [
        [0, 3, 0],
        [0, 3, 0],
        [0, 3, 3],
    ],

    [
        [0, 0, 0],
        [3, 3, 3],
        [3, 0, 0],
    ],

    [
        [3, 3, 0],
        [0, 3, 0],
        [0, 3, 0],
    ],
]

PIECE_O = [
    [
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [0, 4, 4, 0],
        [0, 0, 0, 0],
    ],
]

PIECE_S = [
    [
        [0, 5, 5],
        [5, 5, 0],
        [0, 0, 0],
    ],

    [
        [0, 5, 0],
        [0, 5, 5],
        [0, 0, 5],
    ],

    [
        [0, 0, 0],
        [0, 5, 5],
        [5, 5, 0],
    ],

    [
        [5, 0, 0],
        [5, 5, 0],
        [0, 5, 0],
    ],
]

PIECE_T = [
    [
        [0, 6, 0],
        [6, 6, 6],
        [0, 0, 0],
    ],

    [
        [0, 6, 0],
        [0, 6, 6],
        [0, 6, 0],
    ],

    [
        [0, 0, 0],
        [6, 6, 6],
        [0, 6, 0],
    ],

    [
        [0, 6, 0],
        [6, 6, 0],
        [0, 6, 0],
    ],
]

PIECE_Z = [
    [
        [7, 7, 0],
        [0, 7, 7],
        [0, 0, 0],
    ],

    [
        [0, 0, 7],
        [0, 7, 7],
        [0, 7, 0],
    ],

    [
        [0, 0, 0],
        [7, 7, 0],
        [0, 7, 7],
    ],

    [
        [0, 7, 0],
        [7, 7, 0],
        [7, 0, 0],
    ],
]

DRAW = [
    [
        [1, 1, 1, 1],
    ],

    [
        [2, 0, 0],
        [2, 2, 2],
    ],

    [
        [0, 0, 3],
        [3, 3, 3],
    ],

    [
        [0, 4, 4, 0],
        [0, 4, 4, 0],
    ],

    [
        [0, 5, 5],
        [5, 5, 0],
    ],

    [
        [0, 6, 0],
        [6, 6, 6],
    ],

    [
        [7, 7, 0],
        [0, 7, 7],
    ],
]

KICK_TABLE = [
    # J, L, T, S, Z Tetromino Wall Kick Data
    [
        # 0 >>
        [
            # >> 0
            [],

            # >> 1
            [(-1, 0), (-1, 1), (0, -2), (-1, -2)],

            # >> 2
            [(0, 1), (1, 1), (-1, 1), (1, 0), (-1, 0)],

            # >> 3
            [(1, 0), (1, 1), (0, -2), (1, -2)],
        ],

        # 1 >>
        [
            # >> 0
            [(1, 0), (1, -1), (0, 2), (1, 2)],

            # >> 1
            [],

            # >> 2
            [(1, 0), (1, -1), (0, 2), (1, 2)],

            # >> 3
            [(1, 0), (1, 2), (1, 1), (0, 2), (0, 1)],
        ],

        # 2 >>
        [
            # >> 0
            [(0, -1), (-1, 1), (1, 1), (-1, 0), (1, 0)],

            # >> 1
            [(-1, 0), (-1, 1), (0, -2), (-1, -2)],

            # >> 2
            [],

            # >> 3
            [(1, 0), (1, 1), (0, -2), (1, -2)],
        ],

        # 3 >>
        [
            # >> 0
            [(-1, 0), (-1, -1), (0, 2), (-1, 2)],

            # >> 1
            [(-1, 0), (-1, 2), (-1, 1), (0, 2), (0, 1)],

            # >> 2
            [(-1, 0), (-1, -1), (0, 2), (-1, 2)],

            # >> 3
            [],
        ],
    ],

    # I Tetromino Wall Kick Data
    [
        # 0 >>
        [
            # >> 0
            [],

            # >> 1
            [(-2, 0), (1, 0), (-2, -1), (1, 2)],

            # >> 2
            [],

            # >> 3
            [(-1, 0), (2, 0), (-1, 2), (2, -1)],
        ],

        # 1 >>
        [
            # >> 0
            [(2, 0), (-1, 0), (2, 1), (-1, -2)],

            # >> 1
            [],

            # >> 2
            [(-1, 0), (2, 0), (-1, 2), (2, -1)],

            # >> 3
            [],
        ],

        # 2 >>
        [
            # >> 0
            [],

            # >> 1
            [(1, 0), (-2, 0), (1, -2), (-2, 1)],

            # >> 2
            [],

            # >> 3
            [(2, 0), (-1, 0), (2, 1), (-1, -2)],
        ],

        # 3 >>
        [
            # >> 0
            [(1, 0), (-2, 0), (1, -2), (-2, 1)],

            # >> 1
            [],

            # >> 2
            [(-2, 0), (1, 0), (-2, -1), (1, 2)],

            # >> 3
            [],
        ],
    ]
]

SCORE_TABLE = {
    # Key: (Line clears, T-spin (0: no / 1: mini / 2: full), B2B?)

    # Single, Double, Triple, Tetris
    (1, 0, False): (100, ['    Single!', '']),
    (2, 0, False): (300, ['    Double!', '']),
    (3, 0, False): (500, ['    Triple!', '']),
    (4, 0, False): (800, ['    Tetris!', '']),

    # Mini T-Spin Simple, Single, Double
    (0, 1, False): (100, ['  Mini T-Spin!', '']),
    (1, 1, False): (200, ['  Mini T-Spin', '    Single!']),
    (2, 1, False): (400, ['  Mini T-Spin', '    Double!']),

    # T-Spin Simple, Single, Double, Triple
    (0, 2, False): (400, ['    T-Spin!', '']),
    (1, 2, False): (800, [' T-Spin Single!', '']),
    (2, 2, False): (1200, [' T-Spin Double!', '']),    
    (3, 2, False): (1600, [' T-Spin Triple!', '']),

    # B2B 
    (1, 1, True): (200, ['  B2B Mini', ' T-Spin Single!']), # Mini T-Spin Single
    (2, 1, True): (600, ['  B2B Mini', ' T-Spin Double!']), # Mini T-Spin Double
    (1, 2, True): (1200, ['  Back-2-Back', ' T-Spin Single!']), # T-Spin Single
    (4, 0, True): (1200, ['  Back-2-Back', '    Tetris!']), # Tetris
    (2, 2, True): (1800, ['  Back-2-Back', ' T-Spin Double']), # T-Spin Double
    (3, 2, True): (2400, ['  Back-2-Back', ' T-Spin Triple']), # T-Spin Triple

}

TETROMINOES = [PIECE_I, PIECE_J, PIECE_L, PIECE_O, PIECE_S, PIECE_T, PIECE_Z]
KICKS = [1, 0, 0, None, 0, 0, 0]
SPAWNS = [(3, -1), (3, 0), (3, 0), (3, -1), (3, 0), (3, 0), (3, 0)]
COLORS = [(0, 255, 255), (0, 0, 255), (255, 128, 0), (255, 255, 0), (0, 255, 0), (255, 0, 255), (255, 0, 0)]


class Piece(): pass

class Challenge():
    def __init__(self, time, func, prompt, details):
        self.time = time
        self.on_place_piece = func
        self.prompt = prompt
        self.details = details



running = False

matrix = [[0 for _ in range(10)] for _ in range(20)]
active_piece = None
hold_piece = None

gravity = 30
arr = 0
das = 8
are = 0
ldelay = 30
lresets = 15
sdrop = 0

_gravity = gravity
_das = das
_are = are
_ldelay = ldelay
_lresets = lresets
_hold = True

next = []
input = (0, 0)
drop_pos = 0

score = 0
lines = 0
level = 0

score_message = ['Press R to start', '']

b2b = False
tspin = 0


def start():
    reset()

    spawn_piece(next_piece())



def reset():
    global running
    running = True

    global matrix, active_piece, hold_piece
    matrix = [[0 for _ in range(10)] for _ in range(20)]

    active_piece = Piece()
    hold_piece = None

    global gravity, arr, das, are, ldelay, lresets, sdrop
    gravity = 30
    arr = 2
    das = 10
    are = 0
    ldelay = 30
    lresets = 15
    sdrop = 1

    global _gravity, _das, _are, _ldelay, _lresets, _hold
    _gravity = gravity
    _das = das
    _are = are
    _ldelay = ldelay
    _lresets = lresets
    _hold = True

    global next, input, drop_pos
    next = []
    input = (0, 0)
    drop_pos = 0

    global score, lines, level
    score = 0
    lines = 0
    level = 0

    global score_message
    score_message = ['', '']

    global b2b, tspin
    b2b = False
    tspin = 0



def update():
    if not running:
        return

    global _are
    if active_piece is None:
        if _are == 0:
            spawn_piece(next_piece())
        else: 
            _are -= 1

        return

    global _gravity, gravity
    _gravity -= 1

    global _das, arr
    if _das <= 0:
        move_piece(arr == 0)
        _das = arr

    if input[0] != 0:
        _das -= 1


    global _ldelay
    if on_ground():
        _ldelay -= 1
        if _ldelay <= 0:
            lock_piece()

        _gravity = gravity

    elif _gravity <= 0:
        drop_piece()



def update_input(h_input, v_input):
    global input
    input = (h_input, v_input)



def move_piece(snap = False):
    if active_piece is None:
        return

    global _lresets, _ldelay, ldelay, tspin
    if snap:
        while input[0] != 0 and not is_collision((active_piece.pos[0] + input[0], active_piece.pos[1])):
            if on_ground():
                if _lresets > 1:
                    _ldelay = ldelay
                    _lresets -= 1

            active_piece.pos = (active_piece.pos[0] + input[0], active_piece.pos[1])
            tspin = 0           

    else:
        if is_collision((active_piece.pos[0] + input[0], active_piece.pos[1])) == False:
            if on_ground():
                if _lresets > 1:
                    _ldelay = ldelay
                    _lresets -= 1

            active_piece.pos = (active_piece.pos[0] + input[0], active_piece.pos[1])
            tspin = 0

    global _das, das
    _das = das

    update_drop_pos()



def soft_drop():
    global _gravity, sdrop
    _gravity = min(_gravity, sdrop)

    if sdrop == 0:
        active_piece.pos = (active_piece.pos[0], drop_pos)



def update_drop_pos():
    global drop_pos
    if active_piece is None:
        return

    drop_pos = 0
    while not is_collision((active_piece.pos[0], active_piece.pos[1] + drop_pos + 1)):
        drop_pos += 1

    drop_pos = active_piece.pos[1] + drop_pos



def hard_drop():
    if active_piece is None:
        return

    if drop_pos != active_piece.pos[1]:
        active_piece.pos = (active_piece.pos[0], drop_pos)

        global tspin
        tspin = 0


    lock_piece()



def rotate_piece(dir):
    if active_piece is None:
        return

    original = active_piece.rot
    active_piece.rot = (active_piece.rot + dir) % len(active_piece.piece)

    global tspin
    tspin = -1

    if is_collision(active_piece.pos):
        failed = True
        if KICKS[active_piece.type] is not None:
            for kick in KICK_TABLE[KICKS[active_piece.type]][original][active_piece.rot]:
                newPos = (active_piece.pos[0] + kick[0], active_piece.pos[1] - kick[1])
                if not is_collision(newPos):
                    active_piece.pos = newPos
                    failed = False

                    # used later for tspin check
                    tspin = kick
                    break

        if failed:
            active_piece.rot = original
            return

    if on_ground():
        global _lresets, _ldelay, ldelay
        if _lresets > 1:
            _ldelay = ldelay
            _lresets -= 1

   
    update_drop_pos()



def hold():
    global _hold
    if not _hold:
        return

    global hold_piece, active_piece
    if active_piece is None:
        return

    held = hold_piece if hold_piece is not None else next_piece()
    hold_piece = active_piece.type

    spawn_piece(held)
    _hold = False



def spawn_piece(piece):
    global active_piece
    active_piece = Piece()

    active_piece.type = piece
    active_piece.piece = TETROMINOES[piece]
    active_piece.rot = 0
    active_piece.pos = SPAWNS[piece]

    for i in range(2):
        if is_collision(active_piece.pos):
            active_piece.pos = (active_piece.pos[0], active_piece.pos[1] - 1)
        else:
            break

        if i == 1:
            global running, score_message
            running = False
            score_message = ['   GAME OVER', 'Press R to retry']
            return


    update_drop_pos()

    

    global _gravity, sdrop, gravity
    _gravity = sdrop if input[1] else gravity

    global _lresets, lresets, _ldelay, ldelay
    _lresets = lresets
    _ldelay = ldelay

    if _gravity == 0:
        active_piece.pos = (active_piece.pos[0], drop_pos)

    global _hold
    _hold = True

    global tspin
    tspin = 0



def next_piece():
    global next
    while len(next) <= 7:
        next += list(numpy.random.permutation(7))

    n = next[0]
    next = next[1:]
    return n



def read_next_piece(i = 0):
    return next[i]



def drop_piece():
    if active_piece is None:
        return

    active_piece.pos = (active_piece.pos[0], active_piece.pos[1] + 1)

    global _gravity, sdrop
    _gravity = sdrop if input[1] else gravity

    if _gravity == 0:
        active_piece.pos = (active_piece.pos[0], drop_pos)

    global tspin
    tspin = 0



def lock_piece():
    global active_piece
    for r in range(len(active_piece.piece[0])):
        row = active_piece.pos[1] + r

        for c in range(len(active_piece.piece[0][r])):
            col = active_piece.pos[0] + c

            if active_piece.piece[active_piece.rot][r][c] != 0:
                matrix[row][col] = active_piece.type + 1

    global tspin, b2b, score, score_message, lines, level
    # T-Spin Test
    if active_piece.type == 5 and tspin != 0:
        corners = 0

        if active_piece.pos[0] < 0 or active_piece.pos[0] >= 10 or active_piece.pos[1] < 0 or active_piece.pos[1] >= 20 or matrix[active_piece.pos[1]][active_piece.pos[0]] != 0:
            corners += 1
        if (active_piece.pos[0] + 2) < 0 or (active_piece.pos[0] + 2) >= 10 or active_piece.pos[1] < 0 or active_piece.pos[1] >= 20 or matrix[active_piece.pos[1]][(active_piece.pos[0] + 2)] != 0:
            corners += 1
        if active_piece.pos[0] < 0 or active_piece.pos[0] >= 10 or (active_piece.pos[1] + 2) < 0 or (active_piece.pos[1] + 2) >= 20 or matrix[(active_piece.pos[1] + 2)][active_piece.pos[0]] != 0:
            corners += 1
        if (active_piece.pos[0] + 2) < 0 or (active_piece.pos[0] + 2) >= 10 or (active_piece.pos[1] + 2) < 0 or (active_piece.pos[1] + 2) >= 20 or matrix[(active_piece.pos[1] + 2)][(active_piece.pos[0] + 2)] != 0:
            corners += 1

        if corners >= 3:
            if tspin == -1 or tspin == (1, -1) and active_piece.rot == 2 or tspin == (-1, -1) and active_piece.rot == 2 or tspin == (1, -2) or tspin == (-1, -2):
                tspin = 2
            else:
                tspin = 1
        else:
            tspin = 0

    else:
        tspin = 0

    l = clear_lines()

    if l > 0 and l != 4 and tspin == 0:
        b2b = False

    if l != 0 or tspin != 0:
        s = SCORE_TABLE[(l, tspin, b2b) if l != 0 else (l, tspin, False)]
        score += s[0] * max(1, level)
        score_message = s[1]

    if l == 4 or tspin != 0:
        b2b = True  


    lines += l

    global gravity
    gravity = round(0.12 * (level - 20) * (level - 20)) if level < 20 else 0

    level = lines // 10

    global _are, are
    _are = are

    active_piece = None



def clear_lines():
    global matrix

    count = 0
    for r in range(len(matrix)):
        clear = True
        for c in matrix[r]:
            if c == 0:
                clear = False
                break

        #Clear line
        if clear:
            count += 1
            matrix = [[0 for i in range(10)]] + [matrix[i] for i in range(r)] + [matrix[i] for i in range(r + 1, 20)]

    return count



def is_collision(newPos):
    for r in range(len(active_piece.piece[0])):
        row = newPos[1] + r

        if row < 0:
            continue

        for c in range(len(active_piece.piece[0][r])):
            col = newPos[0] + c

            if active_piece.piece[active_piece.rot][r][c] != 0:
                if row >= 20 or col >= 10 or col < 0:
                    return True

                if matrix[row][col] != 0:
                    return True

    return False



def on_ground():
    return is_collision((active_piece.pos[0], active_piece.pos[1] + 1))



def generate_challenge():
    def tetris_challenge(info, challenge):
        pass
