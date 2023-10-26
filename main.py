import pygame as p

SIZE_WINDOW = [440, 600]
FRAME_COLOR = (0, 250, 220)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1




screen = p.display.set_mode(SIZE_WINDOW)
p.display.set_caption('Snake')

while True:

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()

    screen.fill(FRAME_COLOR)

    for row in range(COUNT_BLOCKS):
        for colomn in range(COUNT_BLOCKS):
            if (row + colomn) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            p.draw.rect(screen, color, (10 + colomn * SIZE_BLOCK + MARGIN * (colomn + 1), 
                                        20 + row * SIZE_BLOCK + MARGIN * (row + 1) , 
                                        SIZE_BLOCK, SIZE_BLOCK))


    p.display.flip()


