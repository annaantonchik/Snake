import pygame as p
p.init()
import random as r
import sys 

WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
FRAME_COLOR = (0, 250, 220)
HEADER_COLOR = (0, 170, 150)
SNAKE_COLOR = (0, 102, 0)
RED = (244, 0, 0)
SIZE_BLOCK = 20
COUNT_BLOCK = 20
MARGIN = 1
HEADER_MARGIN = 70
size_window = [SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK, 
               SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]
screen = p.display.set_mode(size_window)
p.display.set_caption('Snake')
timer = p.time.Clock()
courier = p.font.SysFont('courier', 36, False, False)
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

    def is_inside(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

def get_random_empty_block():
    x = r.randint(0, COUNT_BLOCK - 1)
    y = r.randint(0, COUNT_BLOCK - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = r.randint(0, COUNT_BLOCK - 1)
        empty_block.y = r.randint(0, COUNT_BLOCK - 1)
    return empty_block

def draw_block(color, row, colomn):
    p.draw.rect(screen, color, (SIZE_BLOCK + colomn * SIZE_BLOCK + MARGIN * (colomn + 1), 
                                HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1) , 
                                SIZE_BLOCK, SIZE_BLOCK))

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
apple = get_random_empty_block()
d_row = 0
d_col = 1
total = 0
speed = 1

while True:

    screen.fill(FRAME_COLOR)
    p.draw.rect(screen, HEADER_COLOR, [0, 0, size_window[0], HEADER_MARGIN])

    text_total = courier.render(f'Total: {total}', 0, WHITE)
    text_speed = courier.render(f'Speed: {speed}', 0, WHITE)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (250 + SIZE_BLOCK, SIZE_BLOCK))

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        elif event.type == p.KEYDOWN:
            if event.key == p.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == p.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == p.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == p.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    for row in range(COUNT_BLOCK):
        for colomn in range(COUNT_BLOCK):
            if (row + colomn) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, colomn)
    
    head = snake_blocks[-1]
    if not head.is_inside():
         p.quit()
         sys.exit()

    draw_block(RED, apple.x, apple.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    if apple == head:
        total += 1
        speed = total // 5 + 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()  

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)
        
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    p.display.flip()
    timer.tick(2 + speed)


