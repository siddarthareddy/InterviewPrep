#Time - O(nlog(n) + mlog(m))
#Space - O(1)
def closestPair(array1, array2):
    array1.sort()
    array2.sort()
    smallestPair=[]
    smallest = float("inf")
    idx1 = 0
    idx2 = 0
    while idx1 < len(array1) and idx2 < len(array2):
        firstNum = array1[idx1]
        secondNum = array2[idx2]
        current = abs(secondNum - firstNum)
        if firstNum < secondNum:
            idx1 += 1
        elif secondNum < firstNum:
            idx2 += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

if __name__ == "__main__":
    a = [-1, 5, 10, 20, 28, 3]
    b = [26, 134, 135, 15, 17]
    print(closestPair(a, b))
    a = [-1, 3, 4, 10, 20, 28]
    b = [15, 17, 26, 134, 135]
    print(closestPair(a, b))