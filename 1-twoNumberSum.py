# O(n^2) O(n) O(1)
# O(nlogn) O(log(n))

# #O(n^2) time | O(n) space
def twoNumberSum1(array, targetNum):
    for i in range(len(array) -1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetNum:
                return [firstNum, secondNum]
    return []

#O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

#O(nlogn) time | O(n) space)
def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

if __name__ == "__main__":
    array = [1,23,4,5,6,7,10,-1,11]
    targetSum = 10
    print(twoNumberSum2(array, targetSum))