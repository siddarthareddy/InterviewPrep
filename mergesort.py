#Time - O(n^2)
#Space - O(1)

def heapu(arr):
    heap = []
    for e in arr:
        heapq.heappush(heap, e)
    print(heap)
if __name__ == "__main__":
    array = [2,1,3,5,2,6,8,2]
    a = []
    for i in range(100):
        a.append(i)
    a.reverse()
    array = [7,6,5,4,3,2,1,0,-1,-2,-3]
    # a = [4,3,2,1]
    print(heapu(a))
    print(heapu(array))

