"""
4.1 Route Between Nodes: 
Given a directed graph and two nodes (S and E), design an algorithm ot find out whether there is a route from S to E.
Hints: #127
Q: pg.109
A: pg.241
"""

from Graph import * # graph
from collections import deque # queue

def main():
    dict = createAdjacencyList()
    
    graph = AdjacencyListGraph(dict)
    graph.printGraph()

    # depth first search
    testDFS(graph)

    # depth first search
    testBFS(graph)

def createAdjacencyList():
    dict = {}

    dict[0] = ("a", [1])
    dict[1] = ("b", [2])
    dict[2] = ("c", [0, 3])
    dict[3] = ("d", [2])
    dict[4] = ("e", [6])
    dict[5] = ("f", [4])
    dict[6] = ("g", [5])

    return dict

# Depth First Search Algorithm
# returns true if there is a path between the two nodes or indexes are the same
# recursive solution
def routeDFS(graph, startIndex, endIndex):
    # no routes if graph is empty
    if len(graph.nodes) == 0:
        return False
    elif startIndex >= len(graph.nodes) or endIndex >= len(graph.nodes):
        return False
    # route has been found so return true
    elif startIndex == endIndex:
        return True
    # route has not been found so keep searching through children
    else:
        currentNode = graph.nodes[startIndex]
        graph.visit(currentNode.index)

        isRoute = False

        for i in currentNode.children:
            nextNode = graph.nodes[i]

            if nextNode.visited == False:
                isRoute = routeDFS(graph, nextNode.index, endIndex)
        
        return isRoute

# Breadth First Search Algorithm
# returns true if there is a path between the two nodes or indexes are the same
# iterative solution with queue
def routeBFS(graph, startIndex, endIndex):
    queue = deque()

    # no routes if graph is empty
    if len(graph.nodes) == 0:
        return False
    elif startIndex >= len(graph.nodes) or endIndex >= len(graph.nodes):
        return False
    else:
        currentNode = graph.nodes[startIndex]
        graph.visit(currentNode.index)
        queue.append(currentNode)

        currentIndex = startIndex

        # while queue is not empty
        while not len(queue) == 0:
            nextNode = queue.pop()

            currentIndex = nextNode.index

            if currentIndex == endIndex:
                return True

            for i in nextNode.children:
                node = graph.nodes[i]
                if node.visited == False:
                    graph.visit(node.index)
                    queue.append(node)

        return False

def testDFS(graph):
    print("\n================================\nDFS\n")
    print("0, 2")
    print(routeDFS(graph, 0, 2))
    graph.unvisitAll()

    print("1, 3")
    print(routeDFS(graph, 1, 3))
    graph.unvisitAll()
    
    print("3, 1")
    print(routeDFS(graph, 3, 1))
    graph.unvisitAll()
    
    print("6, 1")
    print(routeDFS(graph, 6, 1))
    graph.unvisitAll()
    
    print("4, 5")
    print(routeDFS(graph, 4, 5))
    graph.unvisitAll()
    
    print("4, 4")
    print(routeDFS(graph, 4, 4))
    graph.unvisitAll()
    
    print("3, 3")
    print(routeDFS(graph, 3, 3))
    graph.unvisitAll()


def testBFS(graph):
    print("\n================================\nBFS\n")
    print("0, 2")
    print(routeBFS(graph, 0, 2))
    graph.unvisitAll()

    print("1, 3")
    print(routeBFS(graph, 1, 3))
    graph.unvisitAll()

    print("3, 1")
    print(routeBFS(graph, 3, 1))
    graph.unvisitAll()

    print("6, 1")
    print(routeBFS(graph, 6, 1))
    graph.unvisitAll()

    print("4, 5")
    print(routeBFS(graph, 4, 5))
    graph.unvisitAll()

    print("4, 4")
    print(routeBFS(graph, 4, 4))
    graph.unvisitAll()

    print("3, 3")
    print(routeBFS(graph, 3, 3))
    graph.unvisitAll()

if __name__ == "__main__":
    main()