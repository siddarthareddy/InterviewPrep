#Time - O(n^2) coz string is immutable and
#coz string concatenation is O(n)
#space - O(n)
def isPalindromeStringConcat(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString


#Time - O(n), Space - O(n)
def isPalindromeReversedChars(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

# Recursion
#O(n) time | O(n) space - call stack
def isPalindromeRec(string, i=0):
    j = len(string) - 1 - i
    return True if i > j else string[i] == string[j] and isPalindromeRec(string, i+1)

# Tail Recursion
#Time - O(n) time
# Space - O(1) as recursive call can replace the existing call
# on the stack, as there is no need to store
def isPalindromeTailRec(string, i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindromeTailRec(string, i+1)


#Iterative
#Time - O(n)
#Space - O(1)
def isPalindromeIter(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

if __name__ == "__main__":
    a = "adsda"
    b = "adsfda"
    print(isPalindromeIter(a))
    print(isPalindromeIter(b))
