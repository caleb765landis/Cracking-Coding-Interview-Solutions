"""
8.1 Triple Step:
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible Paths the child can run up the stairs.
Hints: #152, 178, 217, 237, 262, 359
Q: 134
A: 342

"""

def main():
    testAlgorithm(0)
    testAlgorithm(4)
    testAlgorithm(5)
    testAlgorithm(10)


def testAlgorithm(n):
    cache = {}
    numPaths = countPaths(n, cache)
    print(numPaths[0])

def countPaths(n, cache):
    numPaths = 0
    numPath1, numPath2, numPath3 = 0, 0, 0

    # if n >=1, we can take 1 more step
    if n >= 1:
        # take the step
        numPath1 += 1

        # num of stairs after the step
        tempN = n - 1

        # cache key is number of stairs left
        key = tempN

        # if we have already calculated the number of paths for this number of steps left,
        # then we can just add that calculation to numPath1 from the cache
        if key in cache:
            numPath1 += cache[key]

        # otherwise, we haven't calculated the number of paths for this n yet,
        # so we'll keep recursing, then add the remaining paths to the cache 
        # so we don't have to calculate them again
        else:
            tempSum, cache = countPaths(tempN, cache)
            cache[key] = tempSum
            numPath1 += tempSum

    # algorithm for taking 2 steps is same for jumping 1 step
    if n >= 2:
        numPath2 += 1
        tempN = n - 2

        key = tempN
        if key in cache:
            numPath2 += cache[key]
        else:
            tempSum, cache = countPaths(tempN, cache)
            cache[key] = tempSum
            numPath2 += tempSum

    # algorithm for taking 3 steps is same for jumping 2 steps
    if n >= 3:
        tempN = n - 3
        numPath3 += 1

        key = tempN
        if key in cache:
            numPath3 += cache[key]
        else:
            tempSum, cache = countPaths(tempN, cache)
            cache[key] = tempSum
            numPath3 += tempSum

    # return sum of number of children from each jumpLength
    numPaths = numPath1 + numPath2 + numPath3
    return numPaths, cache


if __name__ == "__main__":
    main()
