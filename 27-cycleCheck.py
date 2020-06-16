def findCycle(arr):
    if checkFor0s(arr):
        return False
    checkedList = []
    for i in arr:
        checkedList.append(0)
    checkedList[0] = 0

    currentIndex = 0

    while(currentIndex != -1):
        currentIndex = move(arr, currentIndex, checkedList)

    return checkCycle(checkedList)

def checkCycle(checkedList):
    for i in checkedList:
        if i!= 1:
            return False
        else:
            return True

def checkFor0s(arr):
    for num in arr:
        if num == 0:
            return True

def move(arr, current, checked):
    val = arr[current]
    newIndex = (current+val)%len(arr)
    if checked[newIndex] == 0:
        checked[newIndex] = 1
        return newIndex
    else:
        return -1

def hasSingleCycle(array):
    numVisited = 0
    currentIdx = 0
    while numVisited < len(array):
        if numVisited > 0 and currentIdx == 0:
            return False
        numVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0

def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0  else nextIdx + len(array)


if __name__ == "__main__":
    print(findCycle([2,3,1,-4,-4,2]))
    print(findCycle([2,3,1,-4,-3,2]))
    print(findCycle([1,0]))
    print(hasSingleCycle([2,3,1,-4,-4,2]))

