"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should 
throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw 
an error or return null.
"""
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.maxValues = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if len(self.maxValues) == 0:
            self.maxValues.append(x)
        else:
            self.maxValues.append(max(x, self.maxValues[-1]))

    def pop(self) -> int:
        self.maxValues.pop()
        return self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def peekMax(self) -> int:
        return self.maxValues[-1]

    def popMax(self) -> int:
        maxIdx = None
        for i in reversed(range(len(self.values))):
            if self.values[i] == self.peekMax():
                maxIdx = i
                break
        result = self.values.pop(maxIdx)
        self.maxValues.pop(maxIdx)
        for i in range(maxIdx, len(self.values)):
            if i == 0:
                self.maxValues[i] = self.values[i]
            else:
                self.maxValues[i] = max(self.maxValues[i-1], self.values[i])
        return result


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()