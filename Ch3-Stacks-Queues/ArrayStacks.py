"""
FixedMultiStack initializes with default parameters of arrSize=30 and numStacks=3
Expects arrSize % numStacks to equal 0, else raises InvalidNumStacksException.

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

        currentIndex = stackStartIndex + self.sizes[stackNum] + 1
        nextIndex = currentIndex - 1
        if self.sizes[stackNum] == 0:
            raise self.EmptyStackException("ERROR: Stack " + str(stackNum) + " is empty.")
        else:
            # can comment out next line to slightly speed up algorithm
            self.arr[nextIndex] = None

            self.sizes[stackNum] -= 1

    def peek(self, stackNum):
        if not self.isEmpty(stackNum):
            stackStartIndex = stackNum * self.stackMaxSize
            return self.arr[stackStartIndex + self.sizes[stackNum]]
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

class DynamicMultiStack:
    def __init__(self, arrSize, numStacks):
        self.arrSize = arrSize
        self.numStacks = numStacks

    def push(self, data):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def isEmpty(self):
        pass

def testFixedMultiStack():
    pass
def testDynamicMultiStack():
    pass

if __name__ == "__main__":
    testFixedMultiStack()
    testDynamicMultiStack()
