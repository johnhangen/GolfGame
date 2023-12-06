import pygame
from pygame.locals import *
from ball import Ball


class App:
    def __init__(self):
        self._title = None
        self._grass = None
        self._sky = None
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 720
        self._clock = None
        self.score = 0
        self.stroke = 0
        self._font = None
        self.ball = None
        self.level = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("GolfGame")
        self._clock = pygame.time.Clock()
        self._running = True
        self._sky = pygame.image.load("images/sky.jpg")
        self._grass = pygame.image.load("images/grass.jpg")
        self._title = pygame.image.load("images/title.png")
        pygame.font.init()
        self._font = pygame.font.SysFont("test", 36)
        self.ball = Ball(100, 650 - 5, 5, (255, 255, 255), self._display_surf)


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and self.level == 0:
                self.level += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.level != 0:
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
        if self.level == 0:
            self._display_surf.blit(self._sky, (0, 0))
            self._display_surf.blit(self._grass, (0, 650))
            self._display_surf.blit(self._grass, (650, 650))
            self._display_surf.blit(self._title, (170, 0))
            self._display_surf.blit(self._font.render("Press Enter to Play", True, (0, 0, 0)), (550, 500))
        elif self.level == 1:
            self._display_surf.blit(self._sky, (0, 0))
            self._display_surf.blit(self._grass, (0, 650))
            self._display_surf.blit(self._grass, (650, 650))
            pygame.draw.rect(self._display_surf, (0, 0, 0), pygame.Rect(1200, 650, 30, 10))
            pygame.draw.line(self._display_surf, (0, 0, 0), (self.ball.xy.x, self.ball.xy.y), (pygame.mouse.get_pos()))
            self._display_surf.blit(self._font.render(f"Score: {self.score}", True, (255, 255, 255)), (10, 10))
            self._display_surf.blit(self._font.render(f"Stroke: {self.stroke}", True, (255, 255, 255)), (10, 35))
            pygame.draw.rect(self._display_surf, (0, 0, 0), pygame.Rect(600, 300, 50, 350))
            self.ball.draw()
        elif self.level == 2:
            self._display_surf.blit(self._sky, (0, 0))
            self._display_surf.blit(self._grass, (0, 650))
            self._display_surf.blit(self._grass, (650, 650))
            pygame.draw.rect(self._display_surf, (0, 0, 0), pygame.Rect(1200, 650, 30, 10))
            pygame.draw.line(self._display_surf, (0, 0, 0), (self.ball.xy.x, self.ball.xy.y), (pygame.mouse.get_pos()))
            self._display_surf.blit(self._font.render(f"Score: {self.score}", True, (255, 255, 255)), (10, 10))
            self._display_surf.blit(self._font.render(f"Stroke: {self.stroke}", True, (255, 255, 255)), (10, 35))
            pygame.draw.rect(self._display_surf, (0, 0, 0), pygame.Rect(600, 300, 50, 350))
            self.ball.draw()

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
