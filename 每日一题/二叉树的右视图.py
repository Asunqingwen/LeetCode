"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):
    input = input.strip()
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = deque()
        stack.append(root)
        result = []
        values = []
        while True:
            values = []
            length = len(stack)
            while length > 0:
                temp_node = stack.popleft()
                length -= 1
                values.append(temp_node.val)
                if temp_node.left:
                    stack.append(temp_node.left)
                if temp_node.right:
                    stack.append(temp_node.right)
            if not values:
                break
            result.append(values[-1])
            values.clear()
        return result


if __name__ == '__main__':
    nums = "1, 2, 3, 4"
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.rightSideView(root)
    print(result)
