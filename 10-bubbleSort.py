# def bubbleSort(array):
#     l = len(array)
#     for i in range(0, l):
#         bubble(array, l - i)
#     return array
#
# def bubble(array, left):
#     for i in range(0, left):
#         k = i
#         while k < left - 1:
#             if array[k] > array[k + 1]:
#                 swap
#             k += 1

# Time O(n^2) | Space O(1)
def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    array = [2,1,3,5,2,6,8,2]
    print(bubbleSort(array))