import pygame

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BALL_RADIUS = 5
HOLE_POSITION = pygame.Rect(1200, 650, 30, 10)
GROUND_LEVEL = 650
FRICTION = 0.995
GRAVITY = pygame.Vector2(0, 30)
MIN_VELOCITY = 20


class Ball:
    def __init__(self, x: int, y: int, radius: int, color: tuple, surface: pygame.Surface):
        self.xy = pygame.Vector2(x, y)
        self.vel_xy = pygame.Vector2(0, 0)
        self.radius = radius
        self.color = color
        self.surface = surface
        self.moving = True

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (int(self.xy.x), int(self.xy.y)), self.radius)

    def rect_bounds(self, x1, y1, x2, y2):
        if y2 > self.xy.y > y1 and x2 > self.xy.x > x1:
            self.vel_xy.x *= -1
        if y2 > self.xy.y > y1 and x2 > self.xy.x > x1:
            self.vel_xy.y *= -1

    def screen_bounds(self):
        if self.xy.x > SCREEN_WIDTH or self.xy.x < 0:
            self.vel_xy.x *= -1
        if self.xy.y < 0 or self.xy.y > GROUND_LEVEL:
            self.vel_xy.y *= -1

    def update(self, dt: float):
        self.vel_xy *= FRICTION
        self.xy += self.vel_xy * dt
        self.vel_xy += GRAVITY * dt

        if abs(self.vel_xy.x) < MIN_VELOCITY and abs(self.vel_xy.y) < MIN_VELOCITY and self.xy.y > GROUND_LEVEL:
            self.vel_xy = pygame.Vector2(0, 0)
            self.moving = True

    def init_move(self, mouse_pos: tuple):
        self.vel_xy = (pygame.Vector2(mouse_pos) - self.xy) * 0.5

    def scored(self):
        self.vel_xy = pygame.Vector2(0, 0)
        self.xy = pygame.Vector2(100, GROUND_LEVEL - BALL_RADIUS)