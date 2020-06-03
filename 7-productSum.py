# Time - O(n) | Space - O(d)

def productSum(arr, level = 1):
    sum = 0
    for i in range(len(arr)):
        if not isinstance(arr[i], list):
            sum += level * arr[i]
        else:
            sum += level * productSum(arr[i],level+1)
    return sum


def productSumElegant(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSumElegant(element, multiplier+1)
        else:
            sum += element
    return sum*multiplier

if __name__ == "__main__":
    arr = [5,2,[7,-1],3,[6,[-13,8],4]]
    print(productSum(arr))