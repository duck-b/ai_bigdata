
import sys
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP, K_SPACE, K_z, K_x, K_RETURN, K_ESCAPE
from time import sleep


# 블록 타입, 방향, 1~7은 색상
BLOCK_DATA = (
    (
        (0, 0, 1, 1, 1, 1, 0, 0, 0),
        (0, 1, 0, 0, 1, 0, 0, 1, 1),
        (0, 0, 0, 1, 1, 1, 1, 0, 0),
        (1, 1, 0, 0, 1, 0, 0, 1, 0),
    ), (
        (2, 0, 0, 2, 2, 2, 0, 0, 0),
        (0, 2, 2, 0, 2, 0, 0, 2, 0),
        (0, 0, 0, 2, 2, 2, 0, 0, 2),
        (0, 2, 0, 0, 2, 0, 2, 2, 0)
    ), (
        (0, 3, 0, 3, 3, 3, 0, 0, 0),
        (0, 3, 0, 0, 3, 3, 0, 3, 0),
        (0, 0, 0, 3, 3, 3, 0, 3, 0),
        (0, 3, 0, 3, 3, 0, 0, 3, 0)
    ), (
        (4, 4, 0, 0, 4, 4, 0, 0, 0),
        (0, 0, 4, 0, 4, 4, 0, 4, 0),
        (0, 0, 0, 4, 4, 0, 0, 4, 4),
        (0, 4, 0, 4, 4, 0, 4, 0, 0)
    ), (
        (0, 5, 5, 5, 5, 0, 0, 0, 0),
        (0, 5, 0, 0, 5, 5, 0, 0, 5),
        (0, 0, 0, 0, 5, 5, 5, 5, 0),
        (5, 0, 0, 5, 5, 0, 0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ), (
        (0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0),
        (0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0)
    )
)

# 블록 클래스
class Block:

    def __init__(self, count):
        self.turn = randint(0, 3)
        self.type = BLOCK_DATA[randint(0, 6)]
        self.data = self.type[self.turn] 
        self.size = int(sqrt(len(self.data)))
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        self.fire = count + INTERVAL
        

    def update(self, count):
        erased = 0
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    if 0 <= self.xpos+x_offset < WIDTH and 0 <= self.ypos+y_offset < HEIGHT:
                        val = BLOCK.data[y_offset*BLOCK.size + x_offset]
                        if val != 0:
                            FIELD[self.ypos+y_offset][self.xpos+x_offset] = val

            erased = erase_line()
            go_next_block(count)

        if self.fire < count:
            self.fire = count + INTERVAL
            self.ypos += 1
        return erased

    def draw(self):
        for index in range(len(self.data)):
            xpos = index % self.size
            ypos = index // self.size
            val = self.data[index]
            if 0 <= ypos + self.ypos < HEIGHT and 0 <= xpos + self.xpos < WIDTH and val != 0:
                x_pos = 25 + (xpos + self.xpos) * 25
                y_pos = 25 + (ypos + self.ypos) * 25
                pygame.draw.rect(SURFACE, COLORS[val], (x_pos, y_pos, 24, 24))

# 줄 지움
def erase_line():
    erased = 0
    ypos = 20
    while ypos >= 0:
        if all(FIELD[ypos]):
            erased += 1
            del FIELD[ypos]
            FIELD.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
        else:
            ypos -= 1
    return erased

# 게임 오버 확인
def is_game_over():
    
    filled = 0
    for cell in FIELD[0]:
        if cell != 0:
            filled += 1
    return filled > 2

# 블록 할당
def go_next_block(count):
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)

# 블록 닿음 확인
def is_overlapped(xpos, ypos, turn):
    global HOLD_STATE
    data = BLOCK.type[turn]
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size):
            if 0 <= xpos+x_offset < WIDTH and 0 <= ypos+y_offset < HEIGHT:
                if data[y_offset*BLOCK.size + x_offset] != 0 and FIELD[ypos+y_offset][xpos+x_offset] != 0:
                    HOLD_STATE = True
                    return True
    return False   


# 블록 홀드
def hold_block(count):
    global BLOCK, HOLD_BLOCK, NEXT_BLOCK, HOLD_STATE
    if HOLD_STATE:
        HOLD_STATE = not HOLD_STATE
        if HOLD_BLOCK != None:
            dump_block = BLOCK
            BLOCK = HOLD_BLOCK
            HOLD_BLOCK = dump_block
            HOLD_BLOCK.xpos = randint(2, 8 - BLOCK.size)
            HOLD_BLOCK.ypos = 1 - BLOCK.size
            del dump_block
        else:
            HOLD_BLOCK = BLOCK
            HOLD_BLOCK.xpos = randint(2, 8 - BLOCK.size)
            HOLD_BLOCK.ypos = 1 - BLOCK.size
            BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
            NEXT_BLOCK = Block(count)

# 게임 초기화
def end_game():
    global WIDTH, HEIGHT, FIELD, INTERVAL, BLOCK, NEXT_BLOCK, HOLD_BLOCK, HOLD_STATE
    
    FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    INTERVAL = 40
    BLOCK = None
    NEXT_BLOCK = None

    HOLD_BLOCK = None
    HOLD_STATE = True

    main()

# 기록 저장
def save_score(name, score):
    global NAME_ITEM
    NAME_ITEM[0] = ' _'
    save_name = f'{NAME_ITEM[name[0][0]]}{NAME_ITEM[name[1][0]]}{NAME_ITEM[name[2][0]]}'
    NAME_ITEM[0] = ' '
    with open('rank.txt', 'r') as file:
        rank = file.readlines()
    rank10 = []

    save_point = 0
    for i in range(1, len(rank)+1):
        rank10.append(rank[i-1].replace('\n','').split(','))
        if score < int(rank10[i-1][1]):
            save_point = i
    rank10.insert(save_point, [save_name, score])
    rank10.pop()

    lines = []
    for r in rank10:
        lines.append(f'{r[0]},{str(r[1]).zfill(5)}\n')
    
    with open('rank.txt', 'w') as file:
        file.writelines(lines)

    end_game()
        

pygame.init()

# 기본설정
SURFACE = pygame.display.set_mode([600, 600])
FPSCLOCK = pygame.time.Clock()
WIDTH = 12
HEIGHT = 22
INTERVAL = 40
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = (
            (0, 0, 0),
            (255, 165, 0),
            (0, 0, 255),
            (0, 255, 255),
            (0, 255, 0),
            (255, 0, 255),
            (255, 255, 0),
            (255, 0, 0),
            (128, 128, 128)
        )
BLOCK = None
NEXT_BLOCK = None

HOLD_BLOCK = None
HOLD_STATE = True
NAME_ITEM = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    # 필요한 변수들
    global INTERVAL
    global FIELD
    count = 0
    score = 0
    name = [[0, True], [0, False], [0, False]]
    change_cell = 0
    select_cell = True
    game_state = {'over': False, 'start': False, 'pause': False, 'key': False, 'rank': False, 'end': False}
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_content = {'over': 'GAME OVER!!', 'start': 'T E T R I S', 'pause': 'PAUSE'}
    start_content = [['PRESS ENTER TO START!', False], ['START', True], ['KEY', False], ['RANK', False], ['QUIT', False]]
    counter = 0
    key_content = ['ARROW KEYS : Move',  'SPACE : Turn', 'Z : Hold', 'X : Pause']
    with open('rank.txt', 'r') as file:
        rank = file.readlines()
    # block 시작
    go_next_block(INTERVAL)

    for ypos in range(HEIGHT):
        for xpos in range(WIDTH):
            FIELD[ypos][xpos] = 8 if xpos == 0 or xpos == WIDTH - 1 else 0
    for index in range(WIDTH):
        FIELD[HEIGHT-1][index] = 8

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        game_state['over'] = is_game_over()
        if game_state['end']:
            for i in range(len(name)):
                if name[i][1]:
                    change_cell = i

            if key == K_DOWN:
                if name[change_cell][0] > 0:
                    name[change_cell][0] -= 1 
                else:
                    name[change_cell][0] = len(NAME_ITEM)-1
            elif key == K_UP:
                if name[change_cell][0] < len(NAME_ITEM)-1:
                    name[change_cell][0] += 1
                else:
                    name[change_cell][0] = 0
            elif key == K_LEFT:
                if change_cell != 0:
                    name[change_cell][1] = False
                    name[change_cell-1][1] = True
                else:
                    name[0][1] = False
                    name[2][1] = True
            elif key == K_RIGHT:
                if change_cell != 2:
                    name[change_cell][1] = False
                    name[change_cell+1][1] = True
                else:
                    name[2][1] = False
                    name[0][1] = True
            elif key == K_RETURN:
                save_score(name, score)
        elif game_state['key']:
            if key == K_ESCAPE:
                game_state['key'] = False
        elif game_state['rank']:
            if key == K_ESCAPE:
                game_state['rank'] = False
        elif not game_state['start']:
        # start 전
            if key == K_DOWN:
                # start 화면에서 키다운
                i = 1
                while True:
                    if start_content[i][1]:
                        start_content[i][1] = False
                        if i == 4:
                            start_content[1][1] = True
                        else:
                            start_content[i+1][1] = True
                        break
                    i += 1
            elif key == K_UP:
                # start 화면에서 키업
                i = 4
                while True:
                    if start_content[i][1]:
                        start_content[i][1] = False
                        if i == 1:
                            start_content[4][1] = True
                        else:
                            start_content[i-1][1] = True
                        break
                    i -= 1
            elif key == K_RETURN:
                # start 화면에서 엔터
                if start_content[1][1]:
                    game_state['start'] = True
                elif start_content[2][1]:
                    game_state['key'] = True
                elif start_content[3][1]:
                    game_state['rank'] = True
                elif start_content[4][1]:
                    pygame.quit()
                    sys.exit()
                
        # Pause 눌렀을 때
        elif game_state['pause']:
            if key == K_x:
                game_state['pause'] = False
        # game over 아닐 때
        elif not game_state['over']:
            count += 5
            if count % 1000 == 0:
                INTERVAL = max(1, INTERVAL - 2)
            erased = BLOCK.update(count)

            # 줄 지움
            if erased > 0:
                score += (2 ** erased) * 100

            # Hold Block
            if key == K_z:
                hold_block(count)

            # BLOCK에서 x, y, turn 받아옴
            next_x, next_y, next_t = BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == K_SPACE:
                pygame.key.set_repeat()
                next_t = (next_t + 1) % 4
            elif key == K_RIGHT:
                next_x += 1
            elif key == K_LEFT:
                next_x -= 1
            elif key == K_DOWN:
                next_y += 1
            elif key == K_x:
                game_state['pause'] = True
            elif key == K_ESCAPE:
                game_state['start'] = False
                game_state['over'] = False
                game_state['end'] = True

            # 움직임
            if not is_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]

        # Field
        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                val = FIELD[ypos][xpos]
                pygame.draw.rect(SURFACE, COLORS[val], (xpos*25 + 25, ypos*25 + 25, 24, 24))

        # Block
        BLOCK.draw()

        # Next Block
        for ypos in range(NEXT_BLOCK.size):
            for xpos in range(NEXT_BLOCK.size):
                val = NEXT_BLOCK.data[xpos + ypos*NEXT_BLOCK.size]
                pygame.draw.rect(SURFACE, COLORS[val], (xpos*25 + 400, ypos*25 + 125, 24, 24))

        # Next Block Box
        next_block_image = smallfont.render('Next', True, (255, 255, 255))
        SURFACE.blit(next_block_image, (425, 75))
        for i in range(6):
            for j in range(5):
                if i == 0 or i == 5 or j == 4:
                    pygame.draw.rect(SURFACE, (128, 128, 128), (375+(i*25), 125+(j*25), 24, 24))
        
        # Hold Block
        if HOLD_BLOCK:
            for ypos in range(HOLD_BLOCK.size):
                for xpos in range(HOLD_BLOCK.size):
                    val = HOLD_BLOCK.data[xpos + ypos*HOLD_BLOCK.size]
                    pygame.draw.rect(SURFACE, COLORS[val], (xpos*25 + 400, ypos*25 + 325, 24, 24))

        # Hold Block Box
        next_block_image = smallfont.render('Hold', True, (255, 255, 255) if HOLD_STATE else (255, 0, 0,))
        SURFACE.blit(next_block_image, (425, 275))
        for i in range(6):
            for j in range(5):
                if i == 0 or i == 5 or j == 4:
                    pygame.draw.rect(SURFACE, (128, 128, 128), (375+(i*25), 325+(j*25), 24, 24))

        # Score Text
        score_str = 'Score: '+str(score).zfill(5)
        score_image = smallfont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (425, 30))

        
        # Center Text
        if not game_state['start'] or game_state['pause'] or game_state['over'] or game_state['key'] or game_state['rank']:
            if game_state['end']:
                SURFACE.fill((0, 0, 0))
                message = largefont.render(f'Your Score: {score}', True, (255, 255, 225))
                message_rect = message.get_rect()
                message_rect.center = (300, 200)
                SURFACE.blit(message, message_rect)
                
                for i in range(len(name)):
                    message = largefont.render(NAME_ITEM[name[i][0]], True, (255, 255, 225))
                    message_rect = message.get_rect()
                    message_rect.center = (210+(i*80), 275)
                    SURFACE.blit(message, message_rect)

                    select_cell = not select_cell if counter % 7 == 0 else select_cell
                    if name[i][1]:
                        pygame.draw.line(SURFACE, (255, 255, 255) if select_cell else (0, 0, 0), (180+(i*80), 300), (240+(i*80), 300))
                    else:
                        pygame.draw.line(SURFACE, (255, 255, 255), (180+(i*80), 300), (240+(i*80), 300))

            elif game_state['key']:
                SURFACE.fill((0, 0, 0))
                message = largefont.render('Key', True, (255, 255, 225))
                message_rect = message.get_rect()
                message_rect.center = (300, 150)
                SURFACE.blit(message, message_rect)

                message = smallfont.render('PRESS ESC TO BACK', True, (128, 128, 128))
                message_rect = message.get_rect()
                message_rect.center = (300, 200)
                SURFACE.blit(message, message_rect)

                for i in range(len(key_content)):
                    message = smallfont.render(key_content[i], True, (255, 255, 255))
                    message_rect = message.get_rect()
                    message_rect.center = (300, 275+(i*50))
                    SURFACE.blit(message, message_rect)

            elif game_state['rank']:
                SURFACE.fill((0, 0, 0))
                message = largefont.render('Rank', True, (255, 255, 225))
                message_rect = message.get_rect()
                message_rect.center = (300, 150)
                SURFACE.blit(message, message_rect)

                message = smallfont.render('PRESS ESC TO BACK', True, (128, 128, 128))
                message_rect = message.get_rect()
                message_rect.center = (300, 200)
                SURFACE.blit(message, message_rect)

                for i in range(len(rank)):
                    dump = rank[i].replace('\n','').split(',')
                    message = smallfont.render(f'{i+1} {dump[0]} {dump[1]}', True, (255, 255, 255))
                    message_rect = message.get_rect()
                    message_rect.center = (150 if i < 5 else 450, 275+((i%5)*50))
                    SURFACE.blit(message, message_rect)


            elif not game_state['start']:
                SURFACE.fill((0, 0, 0))
                
                message = largefont.render(message_content['start'], True, (255, 255, 225))
                message_rect = message.get_rect()
                message_rect.center = (300, 150)
                SURFACE.blit(message, message_rect)

                i = 0
                for content in start_content:
                    if i == 0:
                        content[1] = not content[1] if counter % 15 == 0 else content[1]
                        message = smallfont.render(content[0], True, (128, 128, 128) if content[1] else (0, 0, 0))
                        message_rect = message.get_rect()
                        message_rect.center = (300, 200)
                        SURFACE.blit(message, message_rect)
                    else:
                        message = smallfont.render(content[0], True, (255, 255, 255) if content[1] else (128, 128, 128))
                        message_rect = message.get_rect()
                        message_rect.center = (300, 200+(i*50))
                        SURFACE.blit(message, message_rect)
                    i += 1
            elif game_state['pause']:
                message = largefont.render(message_content['pause'], True, (255, 255, 225))
                message_rect = message.get_rect()
                message_rect.center = (300, 300)
                SURFACE.blit(message, message_rect)
            elif game_state['over']:
                # 랭킹저장

                i = 0
                j = 0
                go_back = True
                while True:
                    pygame.draw.rect(SURFACE, (0, 0, 0), (i*25, j*25, 25, 25))

                    message = largefont.render(message_content['over'], True, (255, 255, 225))
                    message_rect = message.get_rect()
                    message_rect.center = (300, 250)
                    SURFACE.blit(message, message_rect)

                    score_str = 'Score: '+str(score).zfill(5)
                    score_image = smallfont.render(score_str, True, (0, 255, 0))
                    score_rect = score_image.get_rect()
                    score_rect.center = (300, 350)
                    SURFACE.blit(score_image, score_rect)

                    pygame.display.update()
                    sleep(0.01)
                    if go_back:
                        i += 1
                    else:
                        i -= 1
                    if i == 23 or i == 0:
                        j += 1
                        go_back = not go_back
                    if j == 24:
                        l = 0
                        for k in range(len(rank)):
                            dump = rank[k].replace('\n','').split(',')
                            if score > int(dump[1]):
                                l += 1
                                break

                        if l > 0:
                            game_state['end'] = True
                            game_state['start'] = False
                            game_state['over'] = False
                        else :
                            game_state['start'] = False
                            game_state['over'] = False
                            end_game()

                        break

        counter += 1

        # Print
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
