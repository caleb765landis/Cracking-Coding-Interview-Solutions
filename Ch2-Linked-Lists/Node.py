class Node:
    def __init__(self, dataval=None):
        self.dataVal = dataval
        self.prev = None
        self.next = None

def testNode():
    n = Node(5)
    print(n.dataVal)

if __name__ == "__main__":
    testNode()