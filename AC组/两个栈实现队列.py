class Queue:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, x: int) -> None:
        self.stack1.append(x)

    def deleteHead(self) -> int:
        if not self.stack2:
            if not self.stack1:
                return None
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
