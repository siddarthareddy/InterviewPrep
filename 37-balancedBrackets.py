def checkForBalance(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")":"(", "]":"[", "}":"{"}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack.pop() == matchingBrackets[char]:
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    print(checkForBalance("(([]()){})"))
    print(checkForBalance("(([]()){}))"))
    print(checkForBalance(")(([]()){})"))

