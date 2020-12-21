'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 

注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_ = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_ or self.min_[-1] > x:
            self.min_.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_[-1]:
            self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.min())
    print(obj.pop())
    print(obj.top())
    print(obj.min())
