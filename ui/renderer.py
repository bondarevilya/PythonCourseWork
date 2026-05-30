from core.node import Node
from core.edge import Edge
from ui.ui_state import UIState
import math
import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 16, bold=True)#CONST

    def draw_node(self, node: Node, color):
        pygame.draw.circle(
            self.screen,
            color,
            (node.x, node.y),
            10 #CONST
        )

        text = self.font.render(str(node.node_id), True, (0,0,0)) #CONST
        text_rect = text.get_rect(center=(node.x, node.y))
        self.screen.blit(text, text_rect)

    def draw_edge(self, edge: Edge, color):

        pygame.draw.line(
            self.screen,
            color,
            (edge.start_node.x, edge.start_node.y),
            (edge.end_node.x, edge.end_node.y),
            4 #CONST
        )

    def draw_edge_with_weight(self,edge, color):
        start = edge.start_node
        end = edge.end_node

        #DIRECTION
        dx = end.x - start.x
        dy = end.y - start.y

        angle = math.atan2(end.y - start.y, end.x - start.x)
        length = math.hypot(dx, dy)

        if length == 0:
            return

        ux = dx / length
        uy = dy / length

        node_radius = 10 + 4  #CONST 10 + (чуть больше)
        arrow_offset = 4

        #MOVE POINTS
        start_x = start.x + ux * node_radius
        start_y = start.y + uy * node_radius

        end_x = end.x - ux * (node_radius + arrow_offset)
        end_y = end.y - uy * (node_radius + arrow_offset)

        #DRAW EDGE (LINE)
        self.draw_edge(edge, color)

        # DRAW ARROW
        arrow_size = 10 #CONST

        x1 = end_x - arrow_size * math.cos(angle - 0.5)
        y1 = end_y - arrow_size * math.sin(angle - 0.5)

        x2 = end_x - arrow_size * math.cos(angle + 0.5)
        y2 = end_y - arrow_size * math.sin(angle + 0.5)

        pygame.draw.polygon(
            self.screen,
            color,
            [(end.x, end.y), (x1, y1), (x2, y2)]
        )

        #DRAW WEIGHTS (NUMBERS)
        mid_x = (edge.start_node.x + edge.end_node.x) // 2
        mid_y = (edge.start_node.y + edge.end_node.y) // 2 - 19

        text = self.font.render(str(edge.weight), True, color)
        self.screen.blit(text, (mid_x, mid_y))

    def draw_ui(self, screen, state, selected_node):
        font = self.font

        if state == UIState.CREATE_NODES:
            text = "Click to create nodes"
        elif state == UIState.CREATE_EDGES:
            text = "Click to create edges"
        elif state == UIState.SELECT_START:
            text = "Select start node"
        elif state == UIState.SHOW_RESULT:
            text = "Shortest path is shown. Press SPACE to create new graph"

        else:
            text = ""

        ui_text = font.render(text, True,(255,255,255))
        screen.blit(ui_text, (20, 20))

        space_text = font.render("Press SPACE to continue", True,(0,200,30))
        screen.blit(space_text, (20, 50))

        if selected_node is not None:
            node_text = font.render(
                f"Selected node: {selected_node.node_id}",
                True,(255, 200, 0)
            )
            screen.blit(node_text, (20,80))




