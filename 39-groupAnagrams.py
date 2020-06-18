#Time - O(wnlogn + nwlogw)
#Space - O(wn)
def groupAnagrams(words):
    if len(words) == 0:
        return []
    sortedWords = ["".join(sorted(word)) for word in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue
        result.append(currentAnagramGroup)
        currentAnagram = sortedWord
        currentAnagramGroup = [word]

    result.append(currentAnagramGroup)
    return result

#Space - O(wn)
#Time - O(wnlogn)
def group2(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
            continue
        anagrams[sortedWord] = [word]
    print(anagrams)
    print(list(anagrams.values()))
    # result = []
    # for elem in anagrams:
    #     result.append(anagrams[elem])
    # print(result)

if __name__ == "__main__":
    print(groupAnagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
    print(group2(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
