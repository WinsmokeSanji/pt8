import pygame
from pygame import *

from block import Platform, PLATFORM_WIDTH, PLATFORM_HEIGHT, BLOCKdIE, BLOCKtELRPORTM PRNCESS
from monsters import *
from player import Player


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DISPLAY = (WINDOW_HEIGHT, WINDOW_WIDTH)
BACKGROUND_COLOR = '#004400'

FPS= 60
CLOCK = pygame.time.Clock()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0 width, height)

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def apply(self, target):
            self.state = self.camera_func(self.state, target.rect)

    def camera_configure(selfcamera, target_rect):
        l, t _, = target_rect
        _, _, w, h = camera
        l, t = -l +WINDOW_WIDTH / 2, -T + WINDOW_HEIGHT / 2

        l = min(0, l)
        l = max(-(camera.width - WINDOW_WIDTH), l)
        t = max(-(camera.height - WINDOW_HEIGHT), l)
        t = min(0, t)
        return Rect(l, t, w , h)

LEVEL_1 = [
    '------------------------------------',
    '-                                  -',
    '-                                  -',
    '-    --              ---           -',
    '-                                  -',
    '-                                  -',
    '-            ---          --       -',
    '-                                  -',
    '-     ---                          -',
    '-                                  -',
    '-                    ----          -',
    '-                                  -',
    '-      ---                         -',
    '-                             --   -',
    '-                                  -',
    '-                                  -',
    '-                ---               -',
    '------------------------------------'
]


def run_game():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set - caption('Mario')
    bg = Surface(DISPLAY)
    bg.fill(Color(BACKGROUND_COLOR))

    mario = Player(55, 55)
    left = False
    right = False
    up = False
    running = False

    entities = pygame.sprite.Grop()
    animated_entites = pygame.sprite.Grop()
    monsters = pygame.sprite.Grop()
    platforms = list()

    entities.add(mario)

    tp = BlockTeleport(128, 512, 800, 64)
    mn = Monster(200, 200, 2, 3, 150, 15)
    entities.add(tp)
    entities.add(mn)
    platforms.append(tp)
    platforms.append(mn)
    monsters.add(mn)

    def add_monster(monster):










    x, y = 0, 0
    for row symbol in LEVEL_1
        for  row symbol in row:
            it symbol == '_':
                platform = Platform(x, y)
                entities.add(platform)
                platform.append(platform)
            elif symbol == '*':
                block_die = BloclDie(x, y)
                entities.add(block_die)
                platform.append(block_die)
            elif symbol == 'N'
                next_level_teleport = NextLevel(x, y)


            elif sumbol == 'P' :
                princess = Princess(x, y)
                entities.add(princess)
                platforms.append(princess)
                animated_entities.add(princess)

            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while True:










    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit('QUIT')
            screen.blit(bg, (0, 0))
            pygame.display.update()


if __name__ == '__main__':
    run_game()