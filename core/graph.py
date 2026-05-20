class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_graph(self):
        graph_structure = []
        for node in self.nodes:
            node_array = []
            for edge in self.edges:
                if edge.start_node == node:
                    node_array.append((edge.end_node.node_id, edge.weight))
            graph_structure.append(node_array)
        return graph_structure