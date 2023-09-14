"""
8.1 Triple Step:
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
Hints: #152, 178, 217, 237, 262, 359
Q: 134
A: 342
"""

def main():
    testAlgorithm(4)
    testAlgorithm(10)


def testAlgorithm(n):
    numWays = countWays(n)
    print(numWays)

def countWays(n):
    numWays = 0
    sum1, sum2, sum3 = 0, 0, 0

    # print(n)

    if n >= 1:
        temp = n - 1
        sum1 += 1
        sum1 += countWays(temp)

    if n >= 2:
        temp = n - 2
        sum2 += 1
        sum2 += countWays(temp)
    
    if n >= 3:
        temp = n - 3
        sum3 += 1
        sum3 += countWays(temp)

    numWays = sum1 + sum2 + sum3
    return numWays

    # return sum of number of children from each jumpLength

if __name__ == "__main__":
    main()