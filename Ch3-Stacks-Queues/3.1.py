"""
3.1 Three in One: 
Describe how you could use a single array to implement three stacks.
Hints: #2, #12, #38, #58
Q: pg.98
A: pg.227
"""

from ArrayStacks import *

def main():
    testFixedMultiStack()
    testDynamicMultiStack()


def testFixedMultiStack():
    s = FixedMultiStack()
    s.printArr()
    s.printSizes()
    try:
        print(s.peek(0))
    except:
        pass
    finally:
        pass
    print("")

    s.push(1, 0)
    s.push(2, 1)
    s.push(3, 2)
    s.printArr()
    s.printSizes()
    try:
        print(s.peek(0))
    finally:
        pass
    print("")

    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.push(1, 0)
    s.printArr()
    s.printSizes()
    print(s.peek(0))

    try:
        s.push(2, 0)
    except:
        pass
    finally:
        pass

    print("")

    for i in range(0, 10):
        s.pop(0)
    s.printArr()
    s.printSizes()
    # print(s.peek(0))

def testDynamicMultiStack():
    pass

if __name__ == "__main__":
    main()
