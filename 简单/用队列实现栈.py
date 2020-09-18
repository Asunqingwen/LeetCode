"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d1 = deque()
        self.d2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.d2:
            self.d2.append(x)
        else:
            self.d1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.d1:
            while len(self.d1) > 1:
                self.d2.append(self.d1.popleft())
            num = self.d1.popleft()
            self.d1.clear()
        else:
            while len(self.d2) > 1:
                self.d1.append(self.d2.popleft())
            num = self.d2.popleft()
            self.d2.clear()
        return num

    def top(self) -> int:
        """
        Get the top element.
        """
        num = self.pop()
        self.push(num)
        return num

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.d1 and not self.d2


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    param_2 = obj.pop()
    param_4 = obj.empty()
    print(param_2, param_4)
