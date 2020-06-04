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


class MaxStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or x >= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self) -> int:
        pop_num = self.stack1.pop()
        if pop_num == self.stack2[-1]:
            self.stack2.pop()
        return pop_num

    def top(self) -> int:
        return self.stack1[-1]

    def peekMax(self) -> int:
        return self.stack2[-1]

    def popMax(self) -> int:
        pop_item = self.stack2.pop()
        for i in range(len(self.stack1) - 1, -1, -1):
            if self.stack1[i] == pop_item:
                self.stack1.pop(i)
                for j in range(i, len(self.stack1)):
                    if not self.stack2 or self.stack1[j] >= self.stack2[-1]:
                        self.stack2.append(self.stack1[j])
                break
        return pop_item


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
