# LinkedList.py
# A doubly linked list with references to head and tail nodes

from Node import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

        if (self.head != None):
            current = self.head
            while (current.next != None):
                current = current.next

            self.tail = current
        else:
            self.tail = self.head

    def appendValToTail(self, data):
        end = Node(data)

        if self.head == None:
            self.head = end
            self.tail = end

        else :
            self.tail.next = end
            end.prev = self.tail
            
            self.tail = end

    def appendNodeToTail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def deleteNodeWithVal(self, val):
        if (self.head == None): return

        current = self.head

        # while (current.next != None):
        #     if 


        #     current = current.next

    def printVals(self):
        current = self.head

        while (current.next != None):
            print(current.dataVal)
            current = current.next

        print(current.dataVal)

def testLinkedList():
    ll1 = LinkedList()
    try:
        print(ll1.head.dataVal)
    except:
        print("Error: Linked List has no head or head has no dataVal")
    finally:
        pass

    ll1.appendValToTail(1)
    ll1.printVals()

    n1 = Node(1)
    ll2 = LinkedList(n1)
    n2 = Node(2)
    ll2.appendNodeToTail(n2)
    ll2.appendValToTail(3)
    ll2.printVals()

if __name__ == '__main__':
    testLinkedList()
