class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    #Time and Space - O(1)
    def peek(self):
        return self.stack[-1]

    #Time and Space - O(1)
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    #Time and Space - O(1)
    def push(self, val):
        newMinMax = {"min" : val, "max": val}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], newMinMax["min"])
            newMinMax["max"] = max(lastMinMax["max"], newMinMax["max"])
        self.stack.append(val)
        self.minMaxStack.append(newMinMax)

    #Time and Space - O(1)
    def getMin(self):
        return self.minMaxStack[-1]["min"]

    #Time and Space - O(1)
    def getMax(self):
        return self.minMaxStack[-1]["max"]

if __name__ == "__main__":
    stack = MinMaxStack()
    stack.push(5)
    print(stack.getMax())
    print(stack.getMin())
    stack.push(7)
    print(stack.getMax())
    print(stack.getMin())
    stack.push(2)
    print(stack.getMax())
    print(stack.getMin())
    stack.pop()
    print(stack.getMax())
    print(stack.getMin())



