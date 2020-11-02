"""
不使用任何内建的哈希表库设计一个哈希映射

具体地说，你的设计应该包含以下的功能

put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
remove(key)：如果映射中存在这个键，删除这个数值对。

示例：

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);        
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到)
"""


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        def dfs(node: TreeNode):
            if not node:
                node = TreeNode(key, value)
                return node
            if key < node.key:
                node.left = dfs(node.left)
            elif key > node.key:
                node.right = dfs(node.right)
            else:
                node.val = value
            return node

        self.root = dfs(self.root)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        def dfs(node: TreeNode):
            if not node:
                return -1
            if key < node.key:
                return dfs(node.left)
            elif key > node.key:
                return dfs(node.right)
            return node.val

        return dfs(self.root)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        def getMax(node: TreeNode):
            while node.right:
                node = node.right
            return node.key, node.val

        def dfs(node: TreeNode, key: int):
            if not node:
                return None
            if key < node.key:
                node.left = dfs(node.left, key)
            elif key > node.key:
                node.right = dfs(node.right, key)
            else:
                if node.left:
                    node.key, node.val = getMax(node.left)
                    node.left = dfs(node.left, node.key)
                elif node.right:
                    node = node.right
                else:
                    node = None
            return node

        self.root = dfs(self.root, key)


if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    print(obj.get(1))
    obj.put(2, 2)
    print(obj.get(1))
    print(obj.get(3))
    obj.put(2, 1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))
