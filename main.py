import sys, pygame
import tetris

pygame.init()

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

M_BLOCK = 35
M_WIDTH = M_BLOCK * 10
M_HEIGHT = M_BLOCK * 20

def main():
    global SCREEN, MATRIX, HOLD, NEXT, INFO, GAME_FONT
    SCREEN = pygame.display.set_mode([30 * M_BLOCK, M_BLOCK * 23])
    MATRIX = pygame.Surface((M_WIDTH, M_HEIGHT))
    HOLD = pygame.Surface((M_BLOCK * 5, M_BLOCK * 4))
    NEXT = pygame.Surface((M_BLOCK * 5, M_BLOCK * 16))
    INFO = pygame.Surface((M_BLOCK * 7, M_BLOCK * 15))

    CLOCK = pygame.time.Clock()
    GAME_FONT = pygame.freetype.SysFont("Consolas", M_BLOCK * 0.75)
    
    SCREEN.fill((20, 20, 20))

    pygame.draw.rect(SCREEN, WHITE, (10 * M_BLOCK - 3, M_BLOCK - 3, M_WIDTH + 6, M_HEIGHT + 6), 3)
    pygame.draw.rect(SCREEN, WHITE, (22 * M_BLOCK - 3, M_BLOCK - 3, 5 * M_BLOCK + 6, 16 * M_BLOCK + 6), 3)
    pygame.draw.rect(SCREEN, WHITE, (3 * M_BLOCK - 3, M_BLOCK - 3, 5 * M_BLOCK + 6, 4 * M_BLOCK + 6), 3)
    pygame.draw.rect(SCREEN, WHITE, (2 * M_BLOCK - 3, 6 * M_BLOCK - 3, 7 * M_BLOCK + 6, 15 * M_BLOCK + 6), 3)

    while True:
        CLOCK.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        tetris.update()

        read_input(events, pygame.key.get_pressed())

        draw_game()
        pygame.display.update()

def read_input(events, keys):
    tetris.update_input(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN])

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetris.move_piece()
            elif event.key == pygame.K_RIGHT:
                tetris.move_piece()
            elif event.key == pygame.K_z:
                tetris.rotate_piece(-1)
            elif event.key == pygame.K_UP:
                tetris.rotate_piece(1)
            elif event.key == pygame.K_a:
                tetris.rotate_piece(2)
            elif event.key == pygame.K_DOWN:
                tetris.soft_drop()
            elif event.key == pygame.K_c:
                tetris.hold()
            elif event.key == pygame.K_SPACE:
                tetris.hard_drop()
            elif event.key == pygame.K_r:
                tetris.start()

def draw_game():
    MATRIX.fill(BLACK)
    NEXT.fill(BLACK)
    HOLD.fill(BLACK)
    INFO.fill(BLACK)

    draw_matrix()
    draw_active_piece()

    draw_next()
    draw_hold()

    draw_info()

    SCREEN.blit(MATRIX, (10 * M_BLOCK, M_BLOCK))
    SCREEN.blit(NEXT, (22 * M_BLOCK, M_BLOCK))
    SCREEN.blit(HOLD, (3 * M_BLOCK, M_BLOCK))
    SCREEN.blit(INFO, (2 * M_BLOCK, 6 * M_BLOCK))



def draw_grid():
    for x in range(1, 10):
        pygame.draw.line(MATRIX, WHITE, (x * M_BLOCK, 0), (x * M_BLOCK, M_HEIGHT))

    for y in range(1, 20):
        pygame.draw.line(MATRIX, WHITE, (0, y * M_BLOCK), (M_WIDTH, y * M_BLOCK))


def draw_active_piece():
    if tetris.active_piece is None:
        return

    for r in range(len(tetris.active_piece.piece[0])):
        for c in range(len(tetris.active_piece.piece[0][r])):
            if tetris.active_piece.piece[tetris.active_piece.rot][r][c] != 0:
                # Draw ghost
                pygame.draw.rect(MATRIX, (80, 80, 80), ((c + tetris.active_piece.pos[0]) * M_BLOCK, (r + tetris.drop_pos) * M_BLOCK, M_BLOCK, M_BLOCK))

                # Draw piece
                pygame.draw.rect(MATRIX, tetris.COLORS[tetris.active_piece.type], ((c + tetris.active_piece.pos[0]) * M_BLOCK, (r + tetris.active_piece.pos[1]) * M_BLOCK, M_BLOCK, M_BLOCK))


def draw_matrix():
    GAME_FONT.render_to(MATRIX, (8, 8), 'Tetris', WHITE)

    for r in range(len(tetris.matrix)):
        for c in range(len(tetris.matrix[r])):
            if tetris.matrix[r][c] != 0:
                pygame.draw.rect(MATRIX, tetris.COLORS[tetris.matrix[r][c] - 1], (c * M_BLOCK, r * M_BLOCK, M_BLOCK, M_BLOCK))
            # else:   
            #     pygame.draw.rect(MATRIX, WHITE, (c * M_BLOCK + 4, r * M_BLOCK + 4, 3, 3))

            
def draw_next():
    GAME_FONT.render_to(NEXT, (8, 8), 'Next', WHITE)
    spawn = [1, 1]

    for i in range(len(tetris.next)):
        next = tetris.read_next_piece(i)
        piece = tetris.DRAW[next]

        spawn[0] = 0.5 * (5 - len(piece[0]))
        spawn[1] = 1.2 + 3 * i 

        if next == 0:
            spawn[1] += 0.5

        for r in range(len(piece)):
            for c in range(len(piece[r])):
                if piece[r][c] != 0:
                    pygame.draw.rect(NEXT, tetris.COLORS[next], ((c + spawn[0]) * M_BLOCK, (r + spawn[1]) * M_BLOCK, M_BLOCK, M_BLOCK))



def draw_hold():
    GAME_FONT.render_to(HOLD, (8, 8), 'Hold', WHITE)

    hold = tetris.hold_piece
    if hold is None:
        return

    piece = tetris.DRAW[hold]
    height = 1.7 if hold == 0 else 1.2

    for r in range(len(piece)):
        for c in range(len(piece[r])):
            if piece [r][c] != 0:

                pygame.draw.rect(HOLD, tetris.COLORS[hold], ((c + 0.5 * (5 - len(piece[0]))) * M_BLOCK, (r + height) * M_BLOCK, M_BLOCK, M_BLOCK))


def draw_info():
    GAME_FONT.render_to(INFO, (16, M_BLOCK), 'Score', WHITE)
    GAME_FONT.render_to(INFO, (4 * M_BLOCK, M_BLOCK), str(tetris.score), (255, 0, 0))

    GAME_FONT.render_to(INFO, (16, 2 * M_BLOCK), 'Lines', WHITE)
    GAME_FONT.render_to(INFO, (4 * M_BLOCK, 2 * M_BLOCK), str(tetris.lines), (255, 0, 0))

    GAME_FONT.render_to(INFO, (16, 3 * M_BLOCK), 'Level', WHITE)
    GAME_FONT.render_to(INFO, (4 * M_BLOCK, 3 * M_BLOCK), str(tetris.level), (255, 0, 0))

    GAME_FONT.render_to(INFO, (16, 5 * M_BLOCK), tetris.score_message[0], (255, 0, 0))
    GAME_FONT.render_to(INFO, (16, 6 * M_BLOCK), tetris.score_message[1], (255, 0, 0))

 

main()
