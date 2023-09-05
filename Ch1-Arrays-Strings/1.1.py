"""
1.1 Is_Unique: 
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: #44, #117, #132
Q: pg.90
A: pg.192
"""

def main():
    testString = "ThisIsATestString"
    checkString(testString)

    testString = "ThisSTRING"
    checkString(testString)
    
    testString = "string"
    checkString(testString)

def checkString(str):
    if isUniqueChars(str):
        print(str + " is unique")
    else:
        print(str + " is not unique")

# Create a function called isUniqueChars with a string parameter called str
def isUniqueChars(str):
    # create a dictionary called uniqueChars
    uniqueChars = {}

    # Go through each character in the string
    for i in range(0, len(str)):
        # Get current character
        currentChar = str[i]

        # if the character is already in the dictionary, then the string does not have all unique characters
        if currentChar in uniqueChars:
            # So return false
            return False
        
        # Otherwise, add the character to the dictionary
        else:
            uniqueChars[currentChar] = currentChar

    # If every character has been checked, then the string has all unique characters.
    # So return true
    return True

if __name__ == '__main__':      # Runs main() if file wasn't imported.
    main()
