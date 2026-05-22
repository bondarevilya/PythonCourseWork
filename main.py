from core.graph import *
from core.node import *
from core.edge import *
from core.pathfinding  import *

from ui.renderer import *
import pygame


def main():
    pygame.init()

    # SCREEN (ВОТ ЗДЕСЬ СОЗДАЁТСЯ)
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Dijkstra Visualizer")

    clock = pygame.time.Clock()

    # GRAPH
    graph = Graph()

    graph.add_node(Node(0, 100, 100))
    graph.add_node(Node(1, 300, 100))
    graph.add_node(Node(2, 500, 200))

    graph.add_edge(Edge(graph.nodes[0], graph.nodes[1], 5))
    graph.add_edge(Edge(graph.nodes[1], graph.nodes[2], 3))
    graph.add_edge(Edge(graph.nodes[0], graph.nodes[2], 4))

    # RENDERER
    renderer = Renderer(screen)

    # PATHFINDING
    adj = graph.to_adjacency_list()

    start_node_id = 0
   # target_node_id = 2

    dist, prev = Pathfinder.dijkstra(adj, start_node_id)

    #path_ids = Pathfinder.reconstruct_path(prev, target_node_id)

    all_paths = {}

    for target_node_id in range(len(graph.nodes)):
        path_ids = Pathfinder.reconstruct_path(prev, target_node_id)

        path_nodes = [
            graph.get_node_by_id(node_id) for node_id in path_ids
        ]

        all_paths[target_node_id] = path_nodes

    path_edges = set()


    # convert paths [1 -> 2 -> 3] into edges (a,d), (b,c)
    for path in all_paths.values():
        for i in range(len(path) - 1):
            a = path[i].node_id
            b = path[i + 1].node_id

            path_edges.add((a, b))

    # GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # edges
        for edge in graph.edges:

            a = edge.start_node.node_id
            b = edge.end_node.node_id

            if (a, b) in path_edges:
                color = (255, 0, 0)  # if in the final path
            else:
                color = (255, 255, 255)

            renderer.draw_edge_with_weight(edge, color)

        # path
        for path in all_paths.values():
            renderer.draw_path(path, (255, 0, 0))

        #nodes
        for node in graph.nodes:
            renderer.draw_node(node, (254, 255, 255))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()