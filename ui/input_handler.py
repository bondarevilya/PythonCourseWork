import pygame

from ui.ui_state import UIState
from core.edge import Edge


class InputHandler:
    def __init__(self, graph, ui_state):
        self.graph = graph
        self.ui_state = ui_state

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.ui_state.current_state == UIState.CREATE_NODES:
                    self.create_node(mouse_x, mouse_y)

                elif self.ui_state.current_state == UIState.CREATE_EDGES:
                    self.handle_edge_creation(mouse_x, mouse_y)

                elif self.ui_state.current_state == UIState.SELECT_START:
                    self.select_start_node(mouse_x, mouse_y);

    def handle_edge_creation(self, x, y):

        clicked_node = self.graph.get_node_by_position(x, y)

        if clicked_node is None:
            return

        if self.selected_node is None:
            self.selected_node = clicked_node

        else:
            edge = Edge(self.selected_node, clicked_node, 10)

            self.graph.add_edge(edge)

        self.selected_node = None