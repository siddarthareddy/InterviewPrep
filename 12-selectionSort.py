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

if __name__ == "__main__":
    array = [2,1,3,5,2,6,8,2]
    print(selectionSort(array))