#Time - O(N)
#Space - O(N)
def maxSubsetSumNoAdj(arr):
    if len(arr) < 2:
        return max(arr)
    maxSums = arr[:]
    maxSums[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + arr[i])
    return maxSums[-1]

#Time - O(N)
#Space - O(1)
def maxSubsetSumNoAdjOptimal(arr):
    if len(arr) < 3:
        return max(arr)
    second = arr[0]
    first = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        current = max(first, second + arr[i])
        second = first
        first = current
    return first

#Time - O(N)
#Space - O(1)
def maxSubsetSumNoAdjOptimalNeg(arr):
    if len(arr) < 3:
        return max(arr)
    second = arr[0]
    first = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        current = max(first, second + arr[i], arr[i])
        second = first
        first = current
    return first

if __name__ == "__main__":
    a = [7,10,12,7,9,14]
    print(maxSubsetSumNoAdj(a))
    print(maxSubsetSumNoAdjOptimal(a))
    a = [-1, -4, 7, 8, 2, 5, -4]
    print(maxSubsetSumNoAdj(a))
    print(maxSubsetSumNoAdjOptimalNeg(a))