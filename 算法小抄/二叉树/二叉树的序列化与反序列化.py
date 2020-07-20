"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""
from Tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += "n"
            res += " "
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree = data.split()
        if tree[0] == "n":
            return None
        root = TreeNode(int(tree[0]))
        queue = [root]
        i = 1
        while queue:
            cur = queue.pop(0)
            if not cur:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != "n" else None
            cur.right = TreeNode(int(tree[i + 1])) if tree[i + 1] != "n" else None
            # 每次处理两个节点，即左右子树
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root
