#Time O(n), Space-O(n^2)
def getLongestPalindromicSubString(string):
    memoize = {}
    max = float("-inf")
    for i in range(len(string)):
        for j in range(i, len(string)):
            if palindrome(i, j, string, memoize):
                max = j - i + 1 if max < j - i + 1 else max
    return max

def palindrome(i, j, string, memoize):
    id = str(i)+str(j)

    if id in memoize:
        return memoize[id]
    elif i == j:
        return True
    elif i > j:
        return True
    if string[i] == string[j]  and palindrome(i+1, j-1, string, memoize):
        memoize[id] = True
    else:
        memoize[id] = False
    return memoize[id]

#Time - O(n^2), space - O(1)
def getLongest2(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i-1, i+1)
        even = getLongestPalindromeFrom(string, i-1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]

if __name__ == "__main__":
    print(getLongestPalindromicSubString("abaxyzzyxf"))
    print(getLongestPalindromicSubString("abaxyzazyxf"))
    print(getLongestPalindromicSubString('a'))
    print(getLongestPalindromicSubString('aa'))
    print(getLongest2("abaxyzazyxf"))


