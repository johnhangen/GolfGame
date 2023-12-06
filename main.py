import pygame
from ball import Ball

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
MIN_VELOCITY = 1

# load Images
SKY = pygame.image.load("images/sky.jpg")
GRASS = pygame.image.load("images/grass.jpg")

# load fonts
pygame.font.init()  # Initialize the font module
font = pygame.font.SysFont("test", 36)

# load sounds


def render_score(score, font, surface):
    score_text = f"Score: {score}"
    score_surface = font.render(score_text, True, WHITE)
    surface.blit(score_surface, (10, 10))

def render_stroke(score, font, surface):
    stroke_text = f"Stroke: {score}"
    stroke_surface = font.render(stroke_text, True, WHITE)
    surface.blit(stroke_surface, (10, 35))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GolfGame")
    clock = pygame.time.Clock()
    ball = Ball(100, GROUND_LEVEL - BALL_RADIUS, BALL_RADIUS, WHITE, screen)
    running = True
    score = 0
    stroke = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                stroke += 1
                ball.init_move(pygame.mouse.get_pos())

        screen.blit(SKY, (0, 0))
        screen.blit(GRASS, (0, 650))
        screen.blit(GRASS, (650, 650))
        pygame.draw.rect(screen, BLACK, HOLE_POSITION)
        if HOLE_POSITION.collidepoint(ball.xy.x, ball.xy.y):
            score += 1
            stroke = 0
            ball.scored()

        pygame.draw.line(screen, BLACK, (ball.xy.x, ball.xy.y), (pygame.mouse.get_pos()))

        render_score(score, font, screen)
        render_stroke(stroke, font, screen)
        ball.draw()
        ball.update(clock.tick(60) / 1000)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
