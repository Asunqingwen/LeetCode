import math


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.max_nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        if not self.max_nums or self.max_nums[-1] <= x:
            self.max_nums.append(x)

    def pop(self) -> int:
        pop_num = self.nums.pop()
        if pop_num == self.max_nums[-1]:
            self.max_nums.pop()
        return pop_num

    def top(self) -> int:
        return self.nums[-1]

    def getMax(self) -> int:
        return self.max_nums[-1]


if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.push(5)
    maxStack.push(1)
    print(maxStack.getMax())
    print(maxStack.getMax())
