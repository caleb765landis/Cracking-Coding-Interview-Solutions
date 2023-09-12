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
    doubleNum = 0.72
    # expecting output of ERROR
    BinToStr(doubleNum)

    doubleNum = 0.75
    # expecting output of 0.11
    BinToStr(doubleNum)

    doubleNum = -23
    # expecting output of ERROR
    BinToStr(doubleNum)

    doubleNum = 23
    # expecting output of ERROR
    BinToStr(doubleNum)

    doubleNum = 0.375
    # expecting output of 0.011
    BinToStr(doubleNum)

def BinToStr(doubleNum):
    if doubleNum <= 0 or doubleNum >= 1:
        print("ERROR")

    current = doubleNum
    binStr = "0."
    for i in range (32):
        power = -(i + 1)
        factor = math.pow(2, power)

        if factor <= current:
            binStr += "1"
            current -= factor
        elif current == 0:
            break
        else:
            binStr += "0"

    # can trim leading 0s if don't want to show all 32 bits
    if current != 0:
        print("ERROR")
    else:
        print(binStr)

if __name__ == "__main__":
    main()
