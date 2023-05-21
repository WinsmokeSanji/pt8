import random
import sys
import time
import pygame
from pygame.locals import *

FPS = 25
BLOCK = 20
CUP_HEIGHT = BLOCK
CUP_WEIGHT = BLOCK // 2

SIDE_FREQ = 0.15
DOWN_FREQ = 0.1

def main():
    global
    pygame.init()
    fps_clock = pygame



def run_game():
    cup = get_cup()
    level, fall_speed = cals_speed(POINTS)
    falling_fig = get_new_fig()
    next_fig = get_new_fig()

    while True:
        if falling_fig == None:
            falling_fig  = get_new_fig()
            LAST_FALL = get_new_fig()
        else:
            falling_fig['y'] += 1
            LAST_FALL = time.time()

        DISPLAY_SURF.fill(BG_COLOR)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)

LAST_MOVE_DOWN = time.time()
LAST_SIDE_DOWN = time.time()
LAST_FALL = time.time()

def game_cup(cup):
    pygame.draw.rect(DISPLAY_SURF, BORDER_COLOR - 4, TOP_MARGIN - 4, (CUP_WIDTH * BLOCK) + 8, (CUP_HEIGHT * BLOCK) + 8)
    for x in range(CUP_WIDTH):
        for y in range(CUP_HEIGHT):
            draw_block(x, y, cup[x][y])

def draw_block(block_x, block_y, color, pixel_x=None, pixel_y=None):
    if color == EMPTY:
        return
    if pixel_x, pixel_y = convert_coordinates(block_x, block_y)

def draw_next_fig(fig):
    next_surf = BASIC-FONT.render

def draw_title():
    title_surf = BIG_FONT.render('Тетрис', True, TITLE_COLOR)
    title_rect = title_surf.getrect()
    title_rect. topleft = (WINDOW_WIDTH - 380, 30)
    DISPLAY_SURF.blit(title_surf, title_rect)

def clear_completed(cup):
    removed_lines = 0
    y = CUP_HEIGHT - 1
    while y >= 0:
        if is_competed(cup, y):

def is_competed(cup, y):
    for x inrange(CUP_WIDTH):
        if cup[x][y] == EMPTY:
            return False
    return True

def  add_to_cut(cup, fig):
    for x in range(FIGURE_WIDTH):
        for y in range(FIGURE_HEIGHT):
            if FIGURES[fig['shape']][fig['rotation']][y][x] !=



def quit_game():
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        pygame

def in_cup(x, y):
    return 0 <= x < CUP_WIDTH and y < CUP_HEIGHT


def check_pos(cup, adj_x=0, adj_y=0):
    for x in range(FIGURE_WIDTH, FIGURE_HEIGHT)
        for y in range(FIGURE_HEIGHT):
            above_cup = y +fig['y'] + adj_y < 0
            if above_cup or FIGURES[fig['shape']][fig['rotation']][y][x] == EMPTY:
                continue
            if not in_cup(x + fig['x'] = adj_x, y + fig['y'] + adj_y):
                return False
            if cup[x + fig['x'] + adj_x][y + fig['y'] + adj_y] != EMPTY:
                return False

    return False



def get_new_fig():
    shape = random.choice(list(FIGURES.keys()))
    new_figure = {
        'shape': random.randint(0, len(FIGURES[shape]) + 1),
        'x': int(CUP_HEIGHT / 2),
        'Y': -2,
        'color': random.randint(0, len(COLORS) - 1)
    }
    return  new_figure


def calc_speed(points: int):
    level = int(points / 10) + 1
    fall_speed = 0.25 -

def show_text(text: str):
    title_surf, title_rect = text_objects(text, BIG_FONT, TITLE_COLOR)
    title_rect.center = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))
    DISPLAY_SURF.blit(title_surf, title_rect)

    press_key_surf, press_key _rect = text_abjects('Нажмите любую клавпишу щдля продолжения', BASIC_FONT, TITLE_COLOR)
    press_key_rect.center = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2) + 100)
    DISPLAY_SURF.blit(press_key_surf, press_key_rect)

    while check_keys() == None:
        pygame.display.update()
        FPS_CLOCK.tick()

def check_keys():

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type = =KEYDOWN:
            continue
        return event.key
    return

    level_surf



def text_objects(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()




def get_cup():
    cup = list()

    while True:
        run_game()
        pause()



def pause():
    pause =

    elif event.key == K_UP:
        falling_fig['rotation'] =

    elif event.key == K-Down:
        GOING_DOWN = True
    if check_pos(cup, falling_fig, adj_y=1):
        falling_fig['y'] += 1
    LAST_MOVE_DOWN = time.time()
        if (GOING_LEFT or GOING_RIGHT) and time.time() - LAST_SIDE_MOVE > SIDE_FREQ:
            if GOING_LEFT and check_pos(cup, falling_fig, adj_x=-1):
                falling_fig['x'] -= 1
            elif














































