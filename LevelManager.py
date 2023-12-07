import pygame


class LevelManger:

    def __init__(self, surface, level: int = 0):
        self.level = level
        self.surface = surface
        self._title = None
        self._grass = None
        self._sky = None
        self._font = None

    def init_assets(self):
        self._sky = pygame.image.load("images/sky.jpg")
        self._grass = pygame.image.load("images/grass.jpg")
        self._title = pygame.image.load("images/title.png")
        pygame.font.init()
        self._font = pygame.font.SysFont("test", 36)


    def render_level(self, score, stroke, ball):
        if self.level == 0:
            self.render_title()
        elif self.level == 1:
            self.render_l1(score, stroke, ball)


    def render_title(self):
        self.surface.blit(self._sky, (0, 0))
        self.surface.blit(self._grass, (0, 650))
        self.surface.blit(self._grass, (650, 650))
        self.surface.blit(self._title, (170, 0))
        self.surface.blit(self._font.render("Press Enter to Play", True, (0, 0, 0)), (550, 500))

    def render_l1(self, score, stroke, ball):
        self.surface.blit(self._sky, (0, 0))
        self.surface.blit(self._grass, (0, 650))
        self.surface.blit(self._grass, (650, 650))
        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect(1200, 650, 30, 10))
        if ball.moving:
            pygame.draw.line(self.surface, (0, 0, 0), (ball.xy.x, ball.xy.y), (pygame.mouse.get_pos()))
        self.surface.blit(self._font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        self.surface.blit(self._font.render(f"Stroke: {stroke}", True, (255, 255, 255)), (10, 35))
        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect(600, 300, 50, 350))
        ball.draw()
