"""
3.1 Three in One: 
Describe how you could use a single array to implement three stacks.
Hints: #2, #12, #38, #58
Q: pg.98
A: pg.227
"""

from ArrayStacks import *

def main():
    s = FixedMultiStack()
    testStack(s)

    print("""===============================================\nDynamicMultiStack\n""")
    s = DynamicMultiStack()
    testStack(s)


def testStack(s):
    print("Test empty stacks")
    s.printArr()
    s.printSizes()
    try:
        print(s.peek(0))
    except:
        pass
    finally:
        pass
    print("")

    print("test one push in each stacks")
    s.push(1, 0)
    s.push(3, 1)
    s.push(5, 2)
    s.printArr()
    s.printSizes()
    try:
        print(s.peek(0))
    finally:
        pass
    print("")

    print("Push to reach max in first stack")
    for i in range(0, 9):
        s.push(1, 0)
    s.printArr()
    s.printSizes()
    print(s.peek(0))
    print("")

    print("Push even though max is reached")
    try:
        s.push(2, 0)
    except:
        pass
    finally:
        pass
    s.printArr()
    s.printSizes()
    print("")

    print("Pop until stack is empty")
    for i in range(0, 10):
        s.pop(0)
    s.printArr()
    s.printSizes()
    print("")

    print("Try peeking and popping empty stack again")
    try:
        print(s.peek(0))
    except:
        pass
    finally:
        pass

    try:
        s.pop(0)
    except:
        pass
    finally:
        pass
    print("")

    print("Push to reach max in second stack")
    for i in range(0, 9):
        s.push(3, 1)
    s.printArr()
    s.printSizes()
    print(s.peek(1))
    s.printArr()
    s.printSizes()
    print("")

    print("Push even though max is reached")
    try:
        s.push(4, 1)
    except:
        pass
    finally:
        pass
    s.printArr()
    s.printSizes()
    print("")

    print("Pop until stack is empty")
    for i in range(0, 10):
        s.pop(1)
    s.printArr()
    s.printSizes()
    print("")

    print("Try peeking and popping empty stack again")
    try:
        print(s.peek(1))
    except:
        pass
    finally:
        pass

    try:
        s.pop(1)
    except:
        pass
    finally:
        pass
    print("")

    print("Push to reach max in third stack")
    for i in range(0, 9):
        s.push(5, 2)
    s.printArr()
    s.printSizes()
    print(s.peek(2))
    print("")

    print("Push even though max is reached")
    try:
        s.push(6, 2)
    except:
        pass
    finally:
        pass
    s.printArr()
    s.printSizes()
    print("")

    print("Pop until stack is empty")
    for i in range(0, 10):
        s.pop(2)
    s.printArr()
    s.printSizes()
    print("")

    print("Try peeking and popping empty stack again")
    try:
        print(s.peek(2))
    except:
        pass
    finally:
        pass

    try:
        s.pop(2)
    except:
        pass
    finally:
        pass
    print("")

if __name__ == "__main__":
    main()
