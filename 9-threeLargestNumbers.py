# Time - O(n) , Space - O(1)

def findThreeLargestNumbers(array):
    threeLargest = [float("-inf"), float("-inf"), float("-inf")]
    for num in array:
        updateThreeLargest(threeLargest, num)
    return threeLargest

def updateThreeLargest(threeLargest, num):
    if num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, index):
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i + 1]

if __name__ == "__main__":
    array = [1,5,9,14,17,20,37,40,68,98,101,234]
    print(findThreeLargestNumbers(array))