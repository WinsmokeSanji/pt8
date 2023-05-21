from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = '#888888'

JUMP_POWER = 10
GRAVITY = 0.35

ANIMATION_DELAY = 0.1
BASE_DIR = os.path.dirname(__file__)

ANIMATION_RIGHT = [
    (fr'{BASE_DIR}/mario/r1.png')
    (fr'{BASE_DIR}/mario/r2.png')
    (fr'{BASE_DIR}/mario/r3.png')
    (fr'{BASE_DIR}/mario/r4.png')
    (fr'{BASE_DIR}/mario/r5.png')
]
ANIMATION_LEFT = [
    (fr'{BASE_DIR}/mario/l1.png')
    (fr'{BASE_DIR}/mario/l2.png')
    (fr'{BASE_DIR}/mario/l3.png')
    (fr'{BASE_DIR}/mario/l4.png')
    (fr'{BASE_DIR}/mario/l5.png')
]
ANIMATION_JUMP_LEFT = [(fr'{BASE_DIR}/mario/jl.png', 0.1)]
ANIMATION_JUMP_RIGHT = [(fr'{BASE_DIR}/mario/jr.png', 0.1)]

ANIMATION_JUMP = [(fr'{BASE_DIR}/mario/j.png', 0.1)]
ANIMATION_JUMP = [(fr'{BASE_DIR}/mario/0.png', 0.1)]

class Player(sprite.Sprite):
        def __init__(self, x ,y):
            sptite.Sprite.__init__(self)
            self.x_vel = 0
            self.start_x = x

            self.y_vel = 0
            self.start_y = y

            self.on_ground = False

            self.imeg = Surface((WIDTH, HEIGHT))
            self.imege.fill(Color(COLOR))
            self.rect = Rect(x, y, WIDTH, HEIGHT)
            self.image.set_colorkey(Color(COLOR))

            bolt_anim = []
            for animation in ANIMATION_RIGHT:
                bolt_anim.apped((animation, ANIMATION_DELAY))

            if self.on_ground:
                self.y_vel = JUMP_POWER

        if left:
            self.x_vel = -JUMP_POWER

        if right:
            self.x_vel = MOVE_SPEED









































