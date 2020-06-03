class Stack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return None
        length = len(self.queue1)
        for _ in range(length - 1):
            self.queue2.append(self.queue1.pop(0))
        ans = self.queue1[0]
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return ans
