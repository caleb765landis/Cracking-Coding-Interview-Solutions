"""
5.2 Binary to String: 
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print 
the binary representation. If the number cannot be represented accurately in binary with at most 32 
characters, print "ERROR."

Hints: #143, #167, #269, #297
Q: pg.116
A: pg.277
"""

import math

def main():
    doubleNum = 72
    BinToStr(doubleNum)

def BinToStr(doubleNum):
    # if doubleNum <= 0 or doubleNum >= 1:
    #     print("ERROR")

    # power = 0
    current = doubleNum
    binStr = ""
    for i in range (31, -1, -1):
        # print("i: " + str(i))
        
        factor = math.pow(2, i)
        # print("factor: " + str(factor))

        if factor <= current:
            binStr += "1"
            current -= factor
        else:
            binStr += "0"

    # can trim leading 0s if don't want to show all 32 bits

    print(binStr)
    # print(len(binStr))

if __name__ == "__main__":
    main()
