class CQueue:

    def __init__(self):
        self.data1 = list()
        self.data2 = list()

    def appendTail(self, value: int) -> None:
        self.data1.append(value)

    def deleteHead(self) -> int:
        if self.data1:
            while self.data1:
                self.data2.append(self.data1.pop())
            value = self.data2.pop()
            while self.data2:
                self.data1.append(self.data2.pop())
            return value
        else:
            return -1


# Your CQueue object will be instantiated and called as such:
value = 3
obj = CQueue()
obj.appendTail(value)
param_2 = obj.deleteHead()
