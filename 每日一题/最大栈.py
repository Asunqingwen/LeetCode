"""
设计一个最大栈，支持 push、pop、top、peekMax 和 popMax 操作。

 

push(x) -- 将元素 x 压入栈中。
pop() -- 移除栈顶元素并返回这个值。
top() -- 返回栈顶元素。
peekMax() -- 返回栈中最大元素。
popMax() -- 返回栈中最大的元素，并将其删除。如果有多个最大元素，只要删除最靠近栈顶的那个。
 

样例 1:

MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
 

注释:

-1e7 <= x <= 1e7
操作次数不会超过 10000。
当栈为空的时候不会出现后四个操作。
"""
import math


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.max_nums = [-math.inf]

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.max_nums.append(max(self.max_nums[-1], x))

    def pop(self) -> int:
        self.max_nums.pop()
        return self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def peekMax(self) -> int:
        return self.max_nums[-1]

    def popMax(self) -> int:
        max_num = self.max_nums[-1]
        temp = []
        while self.nums[-1] != max_num:
            temp.append(self.nums.pop())
        self.nums.pop()
        map(self.push(), reversed(temp))
        return max_num


if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.push(5)
    maxStack.push(1)
    maxStack.push(5)
    maxStack.top()
    maxStack.popMax()
    maxStack.top()
    maxStack.peekMax()
    maxStack.pop()
    maxStack.top()
