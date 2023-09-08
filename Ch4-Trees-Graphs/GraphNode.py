# Node class for graph data structure
# Expects int index for referencing other nodes, data for node to contain, and an array of child nodes
class GraphNode:
    def __init__(self, index, data, children):
        self.index = index
        self.data = data
        self.children = children
        self.visited = False
