import pygame as p
import sys 

WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
FRAME_COLOR = (0, 250, 220)
HEADER_COLOR = (0, 170, 150)
SNAKE_COLOR = (0, 102, 0)
SIZE_BLOCK = 20
COUNT_BLOCK = 20
MARGIN = 1
HEADER_MARGIN = 70
COUNT_BLOCKS = 20
size_window = [SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK, 
               SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]
screen = p.display.set_mode(size_window)
p.display.set_caption('Snake')
timer = p.time.Clock()
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

def draw_block(color, row, colomn):
    p.draw.rect(screen, color, (SIZE_BLOCK + colomn * SIZE_BLOCK + MARGIN * (colomn + 1), 
                                HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1) , 
                                SIZE_BLOCK, SIZE_BLOCK))

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]

d_row = 0
d_col = 1




while True:

    screen.fill(FRAME_COLOR)
    p.draw.rect(screen, HEADER_COLOR, [0, 0, size_window[0], HEADER_MARGIN])

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

    for row in range(COUNT_BLOCKS):
        for colomn in range(COUNT_BLOCKS):
            if (row + colomn) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, colomn)
    
    head = snake_blocks[-1]
    if not head.is_inside():
         p.quit()
         sys.exit()
         
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)
        
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    p.display.flip()
    timer.tick(2)


