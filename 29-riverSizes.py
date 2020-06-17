def riverSizes(map):
    sizeList = []
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 1:
                sizeList.append(findSize(map, row, col))
    return sizeList

#Time - O(N)

def findSize(map, row, col):
    size = 0
    queue = []
    queue.append([row, col])
    while len(queue) > 0:
        currentNode = queue.pop(0)
        map[currentNode[0]][currentNode[1]] = 0
        size += 1
        #addLeft()
        if currentNode[1] - 1 > 0 and map[currentNode[0]][currentNode[1] - 1] == 1:
            queue.append([currentNode[0], currentNode[1] - 1])
        #addRight()
        if currentNode[1] + 1 < len(map[0]) and map[currentNode[0]][currentNode[1] + 1] == 1:
            queue.append([currentNode[0], currentNode[1] + 1])
        #addTop()
        if currentNode[0] - 1 > 0 and map[currentNode[0] - 1][currentNode[1]] == 1:
            queue.append([currentNode[0] - 1, currentNode[1]])
        #addBottom()
        if currentNode[0] + 1 < len(map) and map[currentNode[0] + 1][currentNode[1]] == 1:
            queue.append([currentNode[0] + 1, currentNode[1]])
    return size
if __name__ == "__main__":
    map = [[1, 0, 0, 1, 0],
           [1, 0, 1, 0, 0],
           [0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 0]]
    print(riverSizes(map))
    map = [[1, 0, 0, 1, 0],
           [1, 0, 1, 0, 0],
           [0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 0]]
    map[0][2] = 1
    print(riverSizes(map))
