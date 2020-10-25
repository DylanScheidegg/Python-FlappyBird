import random
import pygame
from pygame.locals import *

bg = pygame.image.load('bg.jpg')
width = 500  # 500
height = 750
bgX = 0
window = pygame.display.set_mode((width, height))
bg = pygame.transform.scale(bg, (width, height))
bgX2 = bg.get_width()
clock = pygame.time.Clock()


class FlappyBirdMap(object):
    def __init__(self, x):
        self.x = x
        self.arr = []
        self.coll_top = ()
        self.coll_bot = ()

    def generate(self, leng):
        for x in range(leng):
            rand_size = random.randint(50, 500)
            self.arr.append(rand_size)
        print(self.arr)

    def show(self, pipe_height):
        for i in range(len(pipe_height)):
            differ = height - pipe_height[i]
            self.coll_top = (self.x, self.x + 50, 0, pipe_height[i])
            self.coll_bot = ((self.x, pipe_height[i] + 200), (self.x + 50, pipe_height[i] + 200),
                             (self.x + 50, pipe_height[i] + differ), (self.x, pipe_height[i] + differ))
            # if bird.x == self.x + 25:
            # pygame.quit()
            # quit()
            pygame.draw.polygon(window, (10, 175, 50),
                                [(self.x, 0), (self.x, pipe_height[i]), (self.x - 15, pipe_height[i]),
                                 (self.x - 15, pipe_height[i] + 25), (self.x + 65, pipe_height[i] + 25),
                                 (self.x + 65, pipe_height[i]), (self.x + 50, pipe_height[i]), (self.x + 50, 0)])
            pygame.draw.polygon(window, (10, 175, 50),
                                [(self.x, pipe_height[i] + 200), (self.x - 15, pipe_height[i] + 200),
                                 (self.x - 15, pipe_height[i] + 200 - 25), (self.x + 65, pipe_height[i] + 200 - 25),
                                 (self.x + 65, pipe_height[i] + 200), (self.x + 50, pipe_height[i] + 200),
                                 (self.x + 50, pipe_height[i] + differ), (self.x, pipe_height[i] + differ)])

            self.x += 300

    def draw(self):
        self.show(self.arr)


class FlappyBird(object):
    def __init__(self, play_x, play_y):
        self.x = play_x
        self.y = play_y
        self.col_bird = (self.x, self.y, 15, 15)

    def draw(self):
        self.y += 3
        if self.y == height:
            self.y = 100
        pygame.draw.circle(window, (255, 255, 0), (self.x, self.y), 15, 15)


load = FlappyBirdMap(1)
load.generate(100)

bird = FlappyBird(100, load.arr[0] + 80)

pygame.time.set_timer(USEREVENT + 1, 500)
speed = 30
game = True
while game:
    clock.tick(speed)
    # do something with score where the speed increases at a certain score
    bgX -= 1
    bgX2 -= 1

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()

    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    window.blit(bg, (bgX, 0))
    window.blit(bg, (bgX2, 0))

    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == USEREVENT + 1:
            speed += 1
        if pressed[pygame.K_SPACE]:
            bird.y -= 50

    # Update x
    # bird.x = bgX // 4
    load.x = bgX + 450
    load.draw()
    bird.draw()
    pygame.display.update()
