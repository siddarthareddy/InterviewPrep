#Time - O(n^2)
#Space - O(1)
def selectionSort(arr):
    for i in range(len(arr)):
        min = float("inf")
        min_index = -1
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        swap(i, min_index, arr)
    return arr

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def mergeSort(arr):
    mergeSortHelper(arr, 0, len(arr) - 1)
    return arr

def mergeSortHelper(arr, start, end):
    if start >= end:
        return
    elif start == end -1:
        if arr[start] > arr[end]:
            swap(start, end, arr)
            return
    else:
        mergeSortHelper(arr, start, int((start + end)/2))
        mergeSortHelper(arr, int((start+end)/2) + 1, end)
        merge(arr, start, end)

def merge(arr, start, end):
    len1 = int((start + end)/2) - start + 1
    len2 = end - (int((start+end)/2) + 1) + 1
    arr1 = arr[start:int((start + end) / 2)+1]
    arr2 = arr[int((start+end)/2) + 1:end+1]
    i = start
    p = 0
    q = 0

    while p < len1 and q < len2:
        if arr1[p] < arr2[q]:
            arr[i] = arr1[p]
            p += 1
        else:
            arr[i] = arr2[q]
            q += 1
        i += 1

    if q < len2:
        #copy remaining in q to arr
        while(q < len2):
            arr[i] = arr2[q]
            i += 1
            q += 1
    else:
        #copy remaining in p to arr
        while(p < len1):
            arr[i] = arr1[p]
            i += 1
            p += 1

def min(a, b):
    if a < b:
        return a
    return b

if __name__ == "__main__":
    array = [2,1,3,5,2,6,8,2]
    print(selectionSort(array))
    a = []
    for i in range(100):
        a.append(i)
    a.reverse()
    array = [7,6,5,4,3,2,1,0,-1,-2,-3]
    # a = [4,3,2,1]
    print(mergeSort(a))
    print(mergeSort(array))

