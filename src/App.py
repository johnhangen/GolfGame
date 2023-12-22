import pygame
from pygame.locals import *
from ball import Ball
from LevelManager import LevelManger

COLORS_POS = {
    (100, 100): (193, 221, 4),
    (350, 100): (20, 220, 215),
    (600, 100): (238, 58, 163),
    (850, 100): (108, 72, 9),
    (1100, 100): (227, 99, 144),
    (100, 350): (151, 106, 238),
    (350, 350): (239, 73, 236),
    (600, 350): (57, 201, 227),
    (850, 350): (179, 8, 231),
    (1100, 350): (112, 11, 172)
}

class App:
    def __init__(self):
        self._levelManger = None
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 720
        self._clock = None
        self.score = 0
        self.stroke = 0
        self.ball = None
        self.level = 0
        self.color_positions = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("GolfGame")
        self._clock = pygame.time.Clock()
        self._running = True
        self.ball = Ball(100, 650 - 5, 5, (255, 255, 255), self._display_surf)
        self._levelManger = LevelManger(self._display_surf)
        self._levelManger.init_assets()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and self.level == 0:
                self.level += 1
                self._levelManger.level = self.level
            elif event.key == pygame.K_s:
                self.level = 999
            elif event.key == pygame.K_c:
                self.level = 998
            elif event.key == pygame.K_ESCAPE and (self.level == 999 or self.level == 998):
                self.level = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.level not in [0, 999, 998]:
            if self.ball.moving:
                self.ball.moving = False
                self.stroke += 1
                self.ball.init_move(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN and self.level == 999:
            box_size = 50
            print('here')
            for pos, color in COLORS_POS.items():
                if (pos[0] - box_size <= pygame.mouse.get_pos()[0] <= pos[0] + box_size) and (pos[1] - box_size <= pygame.mouse.get_pos()[1] <= pos[1] + box_size):
                    self.ball.color = color
                    print(color)
                    break

    def on_loop(self):
        self._levelManger.level = self.level

        if self.level == 1:
            self.ball.rect_bounds(600, 300, 650, 650)
        elif self.level == 2:
            self.ball.rect_bounds(600, 300, 650, 650)

        self.ball.screen_bounds()
        self.ball.update(self._clock.tick(60) / 1000)

        # ball scored
        if pygame.Rect(1200, 650, 30, 10).collidepoint(self.ball.xy.x, self.ball.xy.y):
            self.score += 1
            self.stroke = 0
            self.level += 1
            self.ball.scored()

    def on_render(self):
        self._levelManger.render_level(self.score, self.stroke, self.ball)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
