from controllers.graph_controller import GraphController
from ui.ui_state import UIState
from core.node import Node


class Appcontroller:
    def __init__(self):
        self.state = UIState.CREATE_NODES
        self.graph_controller = GraphController()

    def handle_click(self, x, y):
        node = self.graph_controller.find_node(x, y)

        if self.state == UIState.CREATE_NODES:
            self.graph_controller.graph.add_node(
                Node(
                    len(self.graph_controller.graph.nodes),
                    x,
                    y
                )
            )
            print(len(self.graph_controller.graph.nodes))

        elif self.state ==UIState.CREATE_EDGES:
            self.graph_controller.handle_edge_click(node)

        elif self.state == UIState.SELECT_START:
            self.graph_controller.start_node = node
            self.graph_controller.selected_node = node

    def handle_key(self, event):
        self.graph_controller.handle_key(event)

    def next_state(self):
        print("SPACE PRESSED, STATE=", self.state)


        if self.state == UIState.CREATE_NODES:
            self.state = UIState.CREATE_EDGES
            print("STATE=", self.state)

        elif self.state == UIState.CREATE_EDGES:
            self.state = UIState.SELECT_START
            print("STATE=", self.state)

        elif self.state == UIState.SELECT_START:
            self.state = UIState.SHOW_RESULT
            self.graph_controller.run_pathfinding()
            print("STATE=", self.state)

        elif self.state == UIState.SHOW_RESULT:
            self.state = UIState.CREATE_NODES
            print("STATE=", self.state)

    def render(self, screen, renderer):
        screen.fill((0,0,0))

        g = self.graph_controller.graph

        for edge in g.edges:
            a = edge.start_node.node_id
            b = edge.end_node.node_id

            color = (255, 0, 0) if (a,b) in self.graph_controller.path_edges else(255,255,255)

            renderer.draw_edge_with_weight(edge, color)

        for node in g.nodes:
            #color = (255,255,255) if (node) in self.graph_controller.path_edges else(255,255,255)
            color = (255,255,255)
            renderer.draw_node(node, color)

        if self.graph_controller.waiting_for_weight:
            text = renderer.font.render(f"Weight: {self.graph_controller.weight_input}",
                                      True,
                                      (140,140,140)
            )
            screen.blit(text, (250, 20))

        renderer.draw_ui(screen, self.state, self.graph_controller.selected_node)