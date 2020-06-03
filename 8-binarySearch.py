# Recursive Time - O(log(n)) | Space - O(log(n))

def bsHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return bsHelper(array, target, left, middle - 1)
    else:
        return bsHelper(array, target, middle+1, right)


def binarySearchR(array, target):
    return bsHelper(array, target, 0, len(array) - 1)


# Iterative - Time - O(log(n)) | Space - O(1)

def binarySearchI(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right)//2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1

if __name__ == "__main__":
    array = [1,5,9,14,17,20,37,40,68,98,101,234]
    print(binarySearchI(array,98))