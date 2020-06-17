class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    #Time - O(N)
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, array)
        return array

    #sift up can make most of the move ups of prev node redundant
    # if the current node is higher and
    #Time - O(log N)
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    #Time - O(long N)
    def siftDown(self, currentIdx, heap):
        childIdx1 = currentIdx * 2 + 1
        while childIdx1 <= len(heap) - 1:
            childIdx2 = currentIdx * 2 + 2 if currentIdx * 2 + 2 < len(heap) else -1
            # print(childIdx2)
            # print(childIdx1)
            if childIdx2 != -1 and heap[childIdx2] < heap[childIdx1]:
                idxToSwap = childIdx2
            else:
                idxToSwap = childIdx1
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childIdx1 = 2 * currentIdx + 1
            else:
                break

    def peek(self):
        return self.heap[0]

    def insert(self, a):
        self.heap.append(a)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, self.heap)
        return valueToRemove

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def printHeap(self):
        return self.heap

if __name__ == "__main__":
    a = MinHeap([3,5,-9,1,3,-2,3,4,7,2,-11,6,3,1,-5,4])
    print(a.peek())
    print(a.printHeap())
    a = MinHeap([11,10,9,8,7,6,5,4,3,2,1])
    print(a.peek())
    print(a.printHeap())
    a = MinHeap([10,9,8,7,6,5,4,3,2,1])
    print(a.peek())
    print(a.printHeap())


