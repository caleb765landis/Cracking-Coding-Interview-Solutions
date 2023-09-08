# Graph data structure organized by an adjacency list.
# Optional parameter for dictionary where each key is the index for the node,
# and each value is a pair tuple with the first item being the data for the node 
# and the second being an array of child nodes

from GraphNode import *

class AdjacencyListGraph:
    def __init__(self, dict = None):
        self.nodes = []

        if dict != None:
            for key, value in dict.items():
                self.nodes.append(GraphNode(key, value[0], value[1]))

    def insert(self, index, data, children):
        self.nodes.append(GraphNode(index, data, children))

    def visit(self, index):
        self.nodes[index].visited = True

    def unvisitAll(self):
        for node in self.nodes:
            node.visited = False

    def printGraph(self):
        if len(self.nodes) == 0:
            print("Graph is empty.")
        else:
            for node in self.nodes:
                print("Index: " + str(node.index))
                print("Data: " + str(node.data))
                print("Children: " + str(node.children))
                print("Visited: " + str(node.visited))
                print("")