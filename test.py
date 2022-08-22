import pygame
import sys
from pygame.locals import *

curx = cury = 0

class draw_array():

    box_color = (0,0,0)
    size = 70
    startx = starty = 0
    num = list()
    screen = 0
    canvas = 0
    font = 0

    # numbers: amount of element
    # direction: 0: horizontal, 1: vertical
    # pass init_val as string
    def __init__(self, window, can, numbers, init_val, x, y, sz = 1, title = ""):
        self.size = self.size * sz
        self.startx = x
        self.starty = y
        self.num = [init_val]*numbers
        self.screen = window
        self.canvas = can
        self.draw()

    def draw(self):
        global curx
        global cury
        self.canvas.fill([200, 224, 218])

        for i in range(len(self.num)):
            tmp = pygame.draw.rect(self.canvas, self.box_color, [self.startx + self.size*i,
                self.starty, self.size, self.size], 1)
            tmp2 = pygame.font.SysFont(None, self.fit_text(len(self.num[i]))).render(self.num[i], True, (0,0,0))
            self.canvas.blit(tmp2, tmp2.get_rect(center = tmp.center))

        self.screen.blit(self.canvas, (curx, cury))
        pygame.display.update()

    # binary search the size of font to fit in the rectangle
    def fit_text(self, length):
        l = 1
        r = 100
        while (l < r-1):
            mid = int((l+r)/2)
            if mid * length <= self.size * 2.4:
                l = mid;
            else:
                r = mid;
        return l

    def add(self, val, pos = -1):
        if pos == -1:
            pos = len(self.num)
        if pos < 0 or pos > len(self.num) :
            print("index out of range : add at position", pos)
            return

        self.num.insert(pos, val)
        self.draw()

    def remove(self, pos):
        if pos < 0 or pos >= len(self.num) :
            print("index out of range : delete at position ", pos)
            return

        del self.num[pos]
        self.draw()

    def update(self, val, pos):
        if pos < 0 or pos >= len(self.num):
            print("index out of range : update at position ", pos)

        self.num[pos] = val
        self.draw()

# def test_algo():


def main():

    global curx
    global cury

    # load
    pygame.init()
    window = pygame.display.set_mode((1000, 800), RESIZABLE)
    pygame.display.set_caption("test window")
    pygame.display.set_icon(pygame.image.load("icon.png"))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 25)
    FPS=30
    window.fill([255,255,255])
    bg = pygame.Surface((100000, 800))
    bg = bg.convert()
    pygame.display.update()
    offset = 5

    # test
    n = input()
    n = int(n)

    arr = draw_array(window, bg, n, "0", 10, 10, 1)

    x = input()
    x = x.split()
    for a in range(n):
        arr.num[a] = x[a]
    arr.draw()

    # scrolling
    click = 0
    move = 0

    # events
    while 1:
        clock.tick(FPS)

        if(click):
            curx += move
            window.blit(bg, (curx, cury))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_d:
                    click = 1
                    move = -1 * offset
                elif event.key == pygame.K_a:
                    click = 1
                    move = offset
                elif event.key == pygame.K_r:
                    arr.remove(5)
                elif event.key == pygame.K_t:
                    arr.add("12")

            if event.type == KEYUP:
                click = 0;
                move = 0

if __name__ == "__main__":
    main();
