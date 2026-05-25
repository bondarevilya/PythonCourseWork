from core.graph import Graph
import pygame
from core.edge import Edge

class GraphController:
    def __init__(self):
        self.graph = Graph()

        self.selected_node = None
        self.start_node = None

        self.pending_start = None
        self.pending_end = None

        self.weight_input = ""
        self.waiting_for_weight = False

        self.all_paths = {}
        self.path_edges  = set()

    def handle_edge_click(self, node):
        if node is None:
            return

        if self.selected_node is None:
            self.selected_node = node
            return

        self.pending_start = self.selected_node
        self.pending_end = node

        self.selected_node = None

        self.weight_input = ""
        self.waiting_for_weight = True

    def handle_key(self, event):
        if not self.waiting_for_weight:
            return

        if event.key == pygame.K_RETURN:

            if self.weight_input == "":
                return

            weight = int(self.weight_input)

            edge = Edge(self.pending_start, self.pending_end, weight)
            self.graph.add_edge(edge)

            self.waiting_for_weight = False
            self.weight_input = ""

        elif event.key == pygame.K_BACKSPACE:

            self.weight_input = self.weight_input[:-1]

        else:
            if event.unicode.isdigit():
                self.weight_input += event.unicode

    def find_node(self, x, y):
        for node in self.graph.nodes:
            dx = node.x - x
            dy = node.y - y

            if dx*dx + dy*dy < 100:
                return node
        return None

    def run_pathfinding(self):
        if self.start_node is None:
            return

        dist, all_paths = self.graph.get_all_paths(self.start_node.node_id)

        self.all_paths = all_paths

        self.path_edges = self.build_path_edges(all_paths)

    def build_path_edges(self, all_paths):
        path_edges = set()

        for path in all_paths.values():

            for i in range(len(path) - 1):
                a = path[i].node_id
                b = path[i + 1].node_id

                path_edges.add((a, b))

        return path_edges