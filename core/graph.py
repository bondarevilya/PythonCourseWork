from core.pathfinding import  Pathfinder

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def to_adjacency_list(self):
        adj = [[] for _ in self.nodes]

        for edge in self.edges:
            u = edge.start_node.node_id
            v = edge.end_node.node_id
            adj[u].append((v, edge.weight))

        return adj

    def get_all_paths(self, start_node_id):
        dist, prev = Pathfinder.dijkstra(self.to_adjacency_list(), start_node_id)

        all_paths = {}

        for target in range(len(self.nodes)):
            path_ids = Pathfinder.reconstruct_path(prev, target)
            all_paths[target] = [self.get_node_by_id(i) for i in path_ids]

        return dist, all_paths