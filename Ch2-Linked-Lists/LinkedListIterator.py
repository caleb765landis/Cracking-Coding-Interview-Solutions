class LinkedListIterator:
    def __init__(self, list):
        self.list = list

        self.current = self.list.head

    class OutOfBoundsException(Exception):
        def __init__(self, message):
            print(message)

    # sets current node to next one in list
    # returns true if iterator can move to next node
    # returns false if current node is None or iterator is at the end
    def next(self):
        if self.current != None:
            if self.current == self.list.tail:
                return False
            else: 
                self.current = self.current.next
                return True
        else:
            return False

    # sets current node to previous one in list
    def previous(self):
        if self.current != None:
            if self.current == self.list.head:
                return False
            else:
                self.current = self.current.previous
                return True
        else:
            return False
        
    # sets current to head of list
    def start(self):
        self.current = self.list.head

    # sets current to tail of list
    def end(self):
        self.current = self.list.tail

    # raises OutOfBoundsException if current node is set to None
    def getCurrentNode(self):
        if self.current != None:
            return self.current
        else: 
            raise self.OutOfBoundsException("Current node is out of bounds of list.")
        
    # raises OutOfBoundsException if current node is set to None
    def getCurrentVal(self):
        if self.current != None:
            return self.current.dataVal
        else:
            raise self.OutOfBoundsException("Current node is out of bounds of list.")
