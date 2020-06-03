#Time - O(n^2)
#Space - O(1)

def insertionSort(array):
    for i in range(len(array)):
        insert(i, array)
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def insert(i, array):
    while(i>0):
        if array[i] < array[i-1]:
            swap(i, i-1, array)
        else:
            break
        i = i -1

if __name__ == "__main__":
    array = [2,1,3,5,2,6,8,2]
    print(insertionSort(array))