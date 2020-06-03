class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        return self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]
