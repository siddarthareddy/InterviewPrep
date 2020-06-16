#Time - O(N^3)
#Space - O(1)
def threeNumberSumBruteForce(array, targetSum):
    matches = []
    array.sort()
    for i in range(0, len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array) - 1):
                if array[i] + array[j] + array[k] == targetSum:
                    matches.append([array[i], array[j], array[k]])
    return matches

#Time - O(N^2)
#Space - O(1)
def threeNumberSum(array, targetSum):
    matches = []
    array.sort()
    for i in range(0, len(array)-2):
        j = i + 1
        k = len(array) - 1
        while j < k:
            sum = array[i] + array[j] + array[k]
            if sum == targetSum:
                matches.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif sum < targetSum:
                j += 1
            elif sum > targetSum:
                k -= 1
    return matches


if __name__ == "__main__":
    array = [1,23,4,5,6,7,10,-1,11]
    targetSum = 10
    print(threeNumberSumBruteForce(array, targetSum))
    print(threeNumberSum(array, targetSum))
    