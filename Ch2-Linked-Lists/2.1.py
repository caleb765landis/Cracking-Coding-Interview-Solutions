"""
2.1 Remoe Dups: 
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40
Q: pg.94
A: pg.208
"""

from LinkedList import LinkedList, createLinkedList, testLinkedList

def main():
    # testLinkedList

    testTwoPointers()

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

if __name__ == "__main__":
    main()