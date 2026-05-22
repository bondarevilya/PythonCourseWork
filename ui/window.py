import pygame


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600)) #CONST
        self.clock = pygame.time.Clock()

    def update(self):
        pass

    def render (self):
        pass