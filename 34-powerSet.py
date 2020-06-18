def powerSet(array):
    includes = []
    set = []
    for i in range(len(array)):
        includes.append(False)
    return powerSetHelper(array, includes, 0, set)

def powerSetHelper(array, includes, index, set):
    if index == len(array):
        elements = []
        for i in range(index):
            if includes[i-1]:
                elements.append(array[i])
        set.append(elements)
    else:
        includes[index] = False
        powerSetHelper(array, includes, index + 1, set)
        includes[index] = True
        powerSetHelper(array, includes, index + 1, set)
    return set

def powerSet2(array):
    subSets = []
    subSets.append([])
    for i in range(len(array)):
        for j in range(pow(2,i)):
            subSets.append(subSets[j]+[array[i]])
    return subSets

def powerSet3(array):
    subSets = []
    subSets.append([])
    for ele in array:
        for j in range(len(subSets)):
        #this range is calculated once, and an iterator is created
        #even as subSets length is increasing with every iteration, range is constant
            currentSubSet = subSets[j]
            subSets.append(currentSubSet+[ele])
    return subSets

if __name__ == "__main__":
    print(powerSet([1,2,3]))
    print(powerSet2([1,2,3]))
    print(powerSet3([1,2,3]))