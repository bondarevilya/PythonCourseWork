from core.node import Node
from core.edge import Edge
import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_node(self, node: Node, color):
        pygame.draw.circle(
            self.screen,
            (255,255,255),
            (node.x, node.y),
            8
        )

    def draw_edge(self, edge: Edge, color):
        pygame.draw.line(
            self.screen,
            (255, 255, 255),
            (edge.start_node.x, edge.start_node.y),
            (edge.end_node.x, edge.end_node.y),
            4
        )

    def draw_path(self, nodes, color):
        pass