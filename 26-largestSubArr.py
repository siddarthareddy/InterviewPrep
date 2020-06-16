def largestSubArrayWrong(arr):
    a = findLargestNeg(arr)

    arr[a[1]:].reverse()
    b = findLargestNeg(arr)

    return sum(arr) - a[0] - b[0]

def findLargestNeg(arr):
    finalNeg = 0
    index = 0
    currentSum = 0
    currentIndex = -1
    for i in arr:
        currentSum += i
        if currentSum < finalNeg:
            finalNeg = currentSum
            index = currentIndex
        currentIndex += 1

    return [finalNeg,currentIndex]

#time O(n)
#space O(1)

def maxSubArray(arr):
    # sum = 0
    # max = 0
    # for i in arr:
    #     sum += i
    #     if sum > max:
    #         max = sum
    #     if sum < 0:
    #         sum = 0
    maxEndingHere = arr[0]
    maxSoFar = maxEndingHere
    for num in arr:
        maxEndingHere = max(maxEndingHere + num, num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return max

if __name__ == "__main__":
    print(largestSubArrayWrong([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))
    print(largestSubArrayWrong([3,-10,4]))

    print(maxSubArray([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))
    print(maxSubArray([3,-10,4]))

