def getBit(num, i=0):
    return (num & (1 << i)) != 0

def setBit(num, i=0):
    return num | (1 << i)

def clearBit(num, i=0):
    mask = ~(1 << i)
    return num & mask

def toggle_bit(value, i=0):
    return value ^ (1 << i)

# clears most significant bit through i (inclusive)
# basically clears all bits left of i
def clearMSBitthroughI(num, i=0):
    mask = (1 << i) - 1
    return num & mask

def clearBitsIthrough0(num, i=0):
    mask = (-1 << (i + 1))
    return num & mask


def main():
    # 11011011
    num = 219
    print(bin(num))

    print(getBit(num, 4))

    num = setBit(num, 2)
    print(num)
    print(bin(num))

    num = clearBit(num, 2)
    print(num)

    num = clearBit(num, 2)
    print(num)

    num = clearMSBitthroughI(num, 4)
    print(bin(num))

    num = 219
    num = clearBitsIthrough0(num, 4)
    print(bin(num))






if __name__ == "__main__":
    main()