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