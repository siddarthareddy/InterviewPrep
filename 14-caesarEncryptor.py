

#Time O(n)
#space O(n)
def encrypt(string, key):
    newLetters = []
    key = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, key))
    return string == "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96+newLetterCode%122)

#Time O(n)
#space O(n)
def encryptArr(string, key):
    newLetters = []
    key = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, key, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <=25 else alphabet[-1 + newLetterCode % 25]

if __name__ == "__main__":
    a = "adsda"
    print(encryptArr(a, 1))