import pygame
from pygame.locals import *
from ball import Ball
from LevelManager import LevelManger


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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.level != 0:
            if self.ball.moving:
                self.ball.moving = False
                self.stroke += 1
                self.ball.init_move(pygame.mouse.get_pos())

    def on_loop(self):
        if self.level == 1:
            self.ball.rect_bounds(600, 300, 650, 650)
        elif self.level == 2:
            self.ball.rect_bounds(600, 300, 650, 650)

        self.ball.screen_bounds()
        self.ball.update(self._clock.tick(60) / 1000)
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
