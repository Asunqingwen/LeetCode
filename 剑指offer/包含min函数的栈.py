class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()
        self.min_value = list()

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.min_value:
            self.min_value.append(min(self.min_value[-1], x))
        else:
            self.min_value.append(x)

    def pop(self) -> None:
        self.data.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.min_value[-1]
