"""
不使用任何内建的哈希表库设计一个哈希集合

具体地说，你的设计应该包含以下的功能

add(value)：向哈希集合中插入一个值。
contains(value) ：返回哈希集合中是否存在这个值。
remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);        
hashSet.add(2);        
hashSet.contains(1);    // 返回 true
hashSet.contains(3);    // 返回 false (未找到)
hashSet.add(2);          
hashSet.contains(2);    // 返回 true
hashSet.remove(2);          
hashSet.contains(2);    // 返回  false (已经被删除)

注意：

所有的值都在 [0, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。
"""


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def add(self, key: int) -> None:
        def dfs(node: TreeNode):
            if not node:
                node = TreeNode(key, key)
                return node
            if key < node.key:
                node.left = dfs(node.left)
            elif key > node.key:
                node.right = dfs(node.right)
            else:
                node.val = node.key
            return node

        self.root = dfs(self.root)

    def remove(self, key: int) -> None:
        def getMax(node: TreeNode):
            while node.right:
                node = node.right
            return node.val

        def dfs(node: TreeNode, key: int):
            if not node:
                return None
            if key < node.key:
                node.left = dfs(node.left, key)
            elif key > node.key:
                node.right = dfs(node.right, key)
            else:
                if node.left:
                    node.key = getMax(node.left)
                    node.val = node.key
                    node.left = dfs(node.left, node.key)
                elif node.right:
                    node = node.right
                else:
                    node = None
            return node

        self.root = dfs(self.root, key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """

        def dfs(node: TreeNode):
            if not node:
                return False
            if key < node.key:
                return dfs(node.left)
            elif key > node.key:
                return dfs(node.right)
            return True

        return dfs(self.root)


if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))
