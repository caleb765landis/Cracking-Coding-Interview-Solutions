"""
2.1 Remove Dups: 
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40
Q: pg.94
A: pg.208
"""

from LinkedList import LinkedList, createLinkedList, testLinkedList, testTwoPointers
from LinkedListIterator import *

def main():
    ll = createLinkedList([0, -4, 3, 3, 185, -4, 8, 29, 0, 1])
    removeDupsBuffer(ll)
    ll.printVals()
    print("")

    ll = createLinkedList([0, -4, 3, 3, 185, -4, 8, 29, 0, 1])
    removeDupsNoBuffer(ll)
    ll.printVals()

    ll = createLinkedList([])
    removeDupsBuffer(ll)
    ll.printVals()
    print("")

    ll = createLinkedList([])
    removeDupsNoBuffer(ll)
    ll.printVals()


# Removes duplicates in O(N) time
# Returns updated list
def removeDupsBuffer(list):
    buffer = {}

    iterator = LinkedListIterator(list)

    # do loop while iterator can move to the next element
    keepGoing = True
    while keepGoing:
        currentVal = iterator.getCurrentVal()
        if currentVal in buffer:
            list.deleteNode(iterator.getCurrentNode())
            list.deleteNode(buffer[currentVal])
        else:
            buffer[currentVal] = iterator.getCurrentNode()

        if not iterator.next():
            keepGoing = False

    return list


# Removes duplicates in O(N^2) time
def removeDupsNoBuffer(list):
    if list.length <= 1:
        return list

    outerIterator = LinkedListIterator(list)
    innerIterator = LinkedListIterator(list)

    keepGoing = True
    while keepGoing:
        # outerVal = list[0]
        outerVal = outerIterator.getCurrentVal()
        # innerVal = list[1]
        innerIterator.next()

        innerIterator.start()
        keepGoingAgain = True
        while keepGoingAgain:
            # print(innerIterator.getCurrentVal())
            innerVal = innerIterator.getCurrentVal()

            # don't check if both iterators are on the same node
            if outerIterator.getCurrentNode() != innerIterator.getCurrentNode():
                if outerVal == innerVal:
                    list.deleteNode(innerIterator.getCurrentNode())
                    list.deleteNode(outerIterator.getCurrentNode())

            if not innerIterator.next():
                keepGoingAgain = False

        if not outerIterator.next():
            keepGoing = False


if __name__ == "__main__":
    main()