import pygame
from ui.renderer import Renderer

from controllers.app_controller import Appcontroller


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600)) #CONST
        pygame.display.set_caption("Dijkstra Visualizer")

        self.clock = pygame.time.Clock()

        self.app = Appcontroller()
        self.renderer = Renderer(self.screen)

    def run(self):

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.app.handle_click(x,y)

                elif event.type == pygame.KEYDOWN:
                    self.app.handle_key(event)

                    if event.key == pygame.K_SPACE:
                        self.app.next_state()

            self.app.render(self.screen, self.renderer)

            pygame.display.flip()
            self.clock.tick(60)