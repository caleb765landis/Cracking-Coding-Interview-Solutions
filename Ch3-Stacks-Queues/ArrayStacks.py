"""
FixedMultiStack initializes with default parameters of arrSize=30 and numStacks=3.

If following Three Stacks in One Array, array slices for each stack follow:
Stack1 = [0, n/3)
Stack2 = [n/3, 2n/3)
Stack3 = [2n/3, n)
"""
class FixedMultiStack:
    class OutOfBoundsException(Exception):
        def __init__(self, message):
            print(message)

    class InvalidNumStacksException(Exception):
        def __init__(self, message):
            print(message)

    class StackFullException(Exception):
        def __init__(self, message):
            print(message)

    class EmptyStackException(Exception):
        def __init__(self, message):
            print(message)

    def __init__(self, arrSize = 30, numStacks = 3):
        self.arrSize = arrSize
        self.numStacks = numStacks

        if arrSize % numStacks == 0:
            self.stackMaxSize = int(self.arrSize / numStacks)
        else:
            raise self.InvalidNumStacksException("ERROR: Cannot divide array evenly among stacks.")
        
        self.arr = [None] * self.arrSize
        self.sizes = [0] * self.numStacks

    def push(self, data, stackNum):
        stackStartIndex = stackNum * self.stackMaxSize

        currentIndex = stackStartIndex + self.sizes[stackNum] - 1
        nextOpenIndex = currentIndex + 1

        if self.sizes[stackNum] == self.stackMaxSize:
            raise self.StackFullException("ERROR: Stack " + str(stackNum) + " is full.")
        else:
            self.arr[nextOpenIndex] = data
            self.sizes[stackNum] += 1

    def pop(self, stackNum):
        stackStartIndex = stackNum * self.stackMaxSize

        currentIndex = stackStartIndex + self.sizes[stackNum] - 1

        if self.sizes[stackNum] == 0:
            raise self.EmptyStackException("ERROR: Stack " + str(stackNum) + " is empty.")
        else:
            # can comment out next line to slightly speed up algorithm
            self.arr[currentIndex] = None

            self.sizes[stackNum] -= 1

    def peek(self, stackNum):
        if not self.isEmpty(stackNum):
            stackStartIndex = stackNum * self.stackMaxSize
            currentIndex = stackStartIndex + self.sizes[stackNum] - 1
            return self.arr[currentIndex]
        else:
            raise self.EmptyStackException("ERROR: Stack " + str(stackNum) + " is empty.")

    def isEmpty(self, stackNum):
        if self.sizes[stackNum] <= 0:
            return True
        else: return False

    def printArr(self):
        print(self.arr)

    def printSizes(self):
        print(self.sizes)


"""
DynamicMultiStack initializes with default parameters of arrSize=30 and numStacks=3.
Expects arrSize % numStacks to equal 0, else raises InvalidNumStacksException.
"""

class DynamicMultiStack:
    class OutOfBoundsException(Exception):
        def __init__(self, message):
            print(message)

    class InvalidNumStacksException(Exception):
        def __init__(self, message):
            print(message)

    class ArrayFullException(Exception):
        def __init__(self, message):
            print(message)

    class EmptyStackException(Exception):
        def __init__(self, message):
            print(message)

    def __init__(self, arrSize = 30, numStacks = 3):
        self.arrSize = arrSize
        self.numStacks = numStacks
        self.numItems = 0

        self.arr = [None] * self.arrSize
        self.sizes = [0] * self.numStacks

        if arrSize % numStacks == 0:
            self.stackMaxSize = int(self.arrSize / numStacks)
        else:
            raise self.InvalidNumStacksException(
                "ERROR: Cannot divide array evenly among stacks.")

        self.startIndexes = [0, self.stackMaxSize, self.stackMaxSize * 2]

    def push(self, data, stackNum):
        currentIndex = self.startIndexes[stackNum] + self.sizes[stackNum] - 1
        nextIndex = (currentIndex + 1) % self.arrSize

        # if array is aready full
        if self.numItems == len(self.arr):
            # raise error
            raise self.ArrayFullException("ERROR: Array is full.")
        # if there is a collision with the next stack
        elif nextIndex == self.startIndexes[(stackNum + 1) % self.numStacks]:
            # shift items in next stack
            self.__shift((stackNum + 1) % self.numStacks)

        # push data to next spot
        self.arr[nextIndex] = data
        # increase size of stack
        self.sizes[stackNum] += 1
        # increase number of items in array
        self.numItems += 1

    def pop(self, stackNum):
        currentIndex = (self.startIndexes[stackNum] + self.sizes[stackNum]) % self.arrSize

        if self.sizes[stackNum] == 0:
            raise self.EmptyStackException(
                "ERROR: Stack " + str(stackNum) + " is empty.")
        else:
            # can comment out next line to slightly speed up algorithm
            self.arr[currentIndex] = None
            # decrease size of this stack
            self.sizes[stackNum] -= 1
            # decrease number of items in array
            self.numItems -= 1

    def peek(self, stackNum):
        if not self.isEmpty(stackNum):
            currentIndex = (self.startIndexes[stackNum] + self.sizes[stackNum] - 1) % self.arrSize
            return self.arr[currentIndex]
        else:
            raise self.EmptyStackException(
                "ERROR: Stack " + str(stackNum) + " is empty.")

    def isEmpty(self, stackNum):
        if self.sizes[stackNum] <= 0:
            return True
        else:
            return False

    def printArr(self):
        print(self.arr)

    def printSizes(self):
        print(self.sizes)

    # shifts all items in stack one spot to the right in the array
    # if this stack runs into next one, shifts that stack too
    def __shift(self, stackNum):
        if self.arrSize == self.numItems:
            raise self.ArrayFullException("ERROR: Array is full.")
        
        topIndex = self.startIndexes[stackNum] + self.sizes[stackNum]
        nextStackIndex = self.startIndexes[(stackNum + 1) % self.numStacks]

        # if index after top of this stack is equal to the start of the next stack,
        # then stacks will collide, so shift the next stack too
        if ((topIndex + 1) % self.arrSize) == nextStackIndex:
            self.__shift((stackNum + 1) % self.arrSize)

        # for every item in this stack,
        # set next spots value in array equal to this spots value
        for i in range(0, self.sizes[stackNum]):
            currentIndex = self.startIndexes[stackNum] + i
            self.arr[currentIndex + 1] = self.arr[currentIndex]

        # increase start index of this stack
        # self.startIndexes[stackNum] = (self.startIndexes[stackNum] + 1) % self.arrSize
        self.startIndexes[stackNum] += 1

