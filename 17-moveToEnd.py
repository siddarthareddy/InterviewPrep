def moveToEnd(arr, element):
    currentIdx = 0
    moved = 0
    while currentIdx < len(arr):
        if arr[currentIdx] != element:
            swap(arr, moved, currentIdx)
            moved += 1
        currentIdx += 1
    return arr


def moveToEndComplicated(arr, element):
    currentIdx = 0
    edge = len(arr) - 1
    while edge > currentIdx:
        while arr[edge] == element:
            edge -= 1
        if currentIdx < edge and arr[currentIdx] == element:
            swap(arr, edge, currentIdx)
        currentIdx += 1
    return arr

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    a = [-1, 2, 5, 10, 2, 20, 2, 28, 3, 2]
    print(moveToEnd(a, 2))
    a = [2,1,2,2,2,3,4,2]
    print(moveToEnd(a, 2))
    a = [2, 1, 2, 2, 2, 3, 4, 2]
    print(moveToEndComplicated(a, 2))