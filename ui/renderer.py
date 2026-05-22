from core.node import Node
from core.edge import Edge
import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 16)

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
            color,
            (edge.start_node.x, edge.start_node.y),
            (edge.end_node.x, edge.end_node.y),
            4
        )

    def draw_edge_with_weight(self,edge, color):
        self.draw_edge(edge, color)

        mid_x = (edge.start_node.x + edge.end_node.x) // 2
        mid_y = (edge.start_node.y + edge.end_node.y) // 2 - 19

        text = self.font.render(str(edge.weight), True, color)

        self.screen.blit(text, (mid_x, mid_y))

    def draw_path(self, nodes, color):

        if len(nodes) < 2:
            return

        for i in range(len(nodes) - 1):
            start_node = nodes[i]
            end_node = nodes[i + 1]

            pygame.draw.line(
                self.screen,
                color,
                (start_node.x, start_node.y),
                (end_node.x, end_node.y),
                4
            )
