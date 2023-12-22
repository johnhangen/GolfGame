import pygame


COLORS = {
    "Sunny Green": (193, 221, 4),
    "Ocean Blue": (20, 220, 215),
    "Magenta Dream": (238, 58, 163),
    "Earth Brown": (108, 72, 9),
    "Rosy Pink": (227, 99, 144),
    "Lavender Purple": (151, 106, 238),
    "Vibrant Violet": (239, 73, 236),
    "Sky Blue": (57, 201, 227),
    "Deep Purple": (179, 8, 231),
    "Royal Blue": (112, 11, 172)
}


class LevelManger:

    def __init__(self, surface, level: int = 0):
        self.level = level
        self.surface = surface
        self._title = None
        self._grass = None
        self._sky = None
        self._font = None

    def init_assets(self):
        self._sky = pygame.image.load("../images/sky.jpg")
        self._grass = pygame.image.load("../images/grass.jpg")
        self._title = pygame.image.load("../images/title.png")
        pygame.font.init()
        self._font = pygame.font.SysFont("test", 35)

    def render_level(self, score, stroke, ball):
        if self.level == 0:
            self.render_title()
        elif self.level == 999:
            self.render_store()
        elif self.level == 998:
            self.render_credits()
        elif self.level == 1:
            self.render_l1(score, stroke, ball)

    def render_title(self):
        self.surface.blit(self._sky, (0, 0))
        self.surface.blit(self._grass, (0, 650))
        self.surface.blit(self._grass, (650, 650))
        self.surface.blit(self._title, (170, 0))
        self.surface.blit(self._font.render("Press Enter to Play", True, (0, 0, 0)), (550, 500))
        self.surface.blit(self._font.render("C for Credits", True, (0, 0, 0)), (50, 670))
        self.surface.blit(self._font.render("S for Store", True, (0, 0, 0)), (1100, 670))

    def render_store(self):
        color_positions = []
        starting_x = 100
        starting_y = 100

        self.surface.blit(self._sky, (0, 0))
        self.surface.blit(self._grass, (0, 650))
        self.surface.blit(self._grass, (650, 650))

        for index, (color_name, color) in enumerate(COLORS.items(), start=1):
            if index == 6:
                starting_y += 250
                starting_x = 100

            pygame.draw.circle(self.surface, (0, 0, 0), (starting_x, starting_y), 32)
            pygame.draw.circle(self.surface, color, (starting_x, starting_y), 30)
            color_positions.append((starting_x, starting_y, color))

            text_surface = self._font.render(color_name, True, (0, 0, 0))
            text_width = text_surface.get_width()
            centered_x = starting_x - (text_width / 2)
            self.surface.blit(text_surface, (centered_x, starting_y+60))

            starting_x += 250

    def render_credits(self):
        self.surface.blit(self._sky, (0, 0))
        self.surface.blit(self._grass, (0, 650))
        self.surface.blit(self._grass, (650, 650))
        self.surface.blit(self._font.render("By: Jack Hangen", True, (0, 0, 0)), (550, 300))
        self.surface.blit(self._font.render("I did it all", True, (0, 0, 0)), (590, 330))

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
