def levDist1(str1, str2):
    str2 = " "+str2
    str1 = " "+str1
    ld = [[0 for i in range(len(str2))] for j in range(len(str1))]
    ld[0] = [i for i in range(len(str2))]
    for i in range(len(str1)):
        ld[i][0] = i
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            #print(str1[j-1]+str2[i-1])
            if str2[j] == str1[i]:
                ld[i][j] = ld[i-1][j-1]
                #print("equal")
            else:
                ld[i][j] = min(ld[i-1][j], ld[i][j-1], ld[i-1][j-1])+1
                #print("notequal")
            #print(str(ld[i][j])+" "+str(i)+str1[i]+" "+str(j)+str2[j])
    #print(ld)
    return ld[len(str1)-1][len(str2)-1]

def levDist2(str1, str2):
    small = str1 if len(str2) > len(str1) else str2
    big = str1 if len(str1) >= len(str2) else str2

    even = [i for i in range(len(small) + 1)]
    odd = [0 for i in range(len(small) + 1)]

    for i in range(1, len(big) +1):
        if i%2 == 1:
            current = odd
            prev = even
        else:
            current = even
            prev = odd
        current[0] = i
        for j in range(1,len(small) + 1):
            if big[i-1] == small[j-1]:
                current[j] = prev[j-1]
            else:
                current[j-1] = min(prev[j], prev[j-1], current[j-1]) + 1
    print(even)
    print(odd)
    return even[-1] if len(big)%2 == 0 else odd[-1]
if __name__ == "__main__":
    print(levDist1("abc", "yabd"))
    print(levDist2("abc", "yabd"))
