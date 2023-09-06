# LinkedList.py
# A doubly linked list with references to head and tail nodes

from Node import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

        self.length = 0

        if (self.head != None):
            current = self.head
            self.length += 1

            while (current.next != None):
                current = current.next
                self.length += 1

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

        self.length += 1

    def appendNodeToTail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

    # Deletes a node in the linked list
    # Assumes node is a valid node that is part of the list
    def deleteNode(self, node):
        # if deleting head
        if node == self.head:
            # and if head has nodes after it
            if node.next != None:
                # set next node to be head
                self.head = node.next
                node.next.prev = None
                self.length -= 1
                return
            # otherwise set head to none
            else:
                self.head = None
                self.length -= 1
                return

        # if deleting tail
        if node == self.tail:
            # and if tail has nodes before it
            if node.prev != None:
                # set the new tail to be current tail's previous node
                self.tail = node.prev
                node.prev.next = None
                self.length -= 1
                return
            # otherwise set tail to None
            else:
                self.tail = None
                self.length -= 1
                return

        # Node must not be head or tail,
        # so set next and prev values of neighbor nodes
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def printVals(self):
        if self.head == None:
            print("No nodes in list.")
            return

        current = self.head

        while (current.next != None):
            print(current.dataVal)
            current = current.next

        print(current.dataVal)

def createLinkedList(list):
    ll = LinkedList()

    for item in list:
        ll.appendValToTail(item)

    return ll

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
    print("Length: " + str(ll1.length))
    print("")

    ll1.deleteNode(ll1.head)
    ll1.printVals()
    print("Length: " + str(ll1.length))
    print("")

    n1 = Node(1)
    ll2 = LinkedList(n1)
    n2 = Node(2)
    ll2.appendNodeToTail(n2)
    ll2.appendValToTail(3)
    ll2.printVals()
    print("Length: " + str(ll2.length))
    print("")

    ll2.deleteNode(n2)
    ll2.printVals()
    print("Length: " + str(ll2.length))
    print("")

    ll2.deleteNode(ll2.tail)
    ll2.printVals()
    print("Length: " + str(ll2.length))
    print("")

    ll2.deleteNode(ll2.tail)
    ll2.printVals()
    print("Length: " + str(ll2.length))
    print("")

    n1 = Node(1)
    ll2 = LinkedList(n1)
    n2 = Node(2)
    ll2.appendNodeToTail(n2)
    ll2.appendValToTail(3)
    ll2.printVals()
    print("Length: " + str(ll2.length))
    print("")

    ll2.deleteNode(ll2.head)
    ll2.printVals()
    print("Length: " + str(ll2.length))
    print("")

    ll3 = createLinkedList([9, 8, 7, 6, 5, 4, 3])
    ll3.printVals()
    print("")


def testTwoPointers():
    ll = createLinkedList([9, 8, 7, 6, 5, 4, 3, 2])
    fastPtr = ll.head
    slowPtr = ll.head

    fastPtrIndex = 1

    for i in range(0, ll.length):
        print(slowPtr.dataVal)
        print(fastPtr.dataVal)
        print("")

        slowPtr = slowPtr.next
        fastPtrIndex += 2

        if fastPtrIndex >= ll.length:
            fastPtr = ll.head
            fastPtrIndex = 1
        else:
            fastPtr = fastPtr.next.next

if __name__ == '__main__':
    testLinkedList()
    testTwoPointers()
