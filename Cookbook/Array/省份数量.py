'''
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

 

示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
 

提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
from typing import List


class Solution:
    def __init__(self):
        self.count = 0
        self.rank = []

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(num: int):
            if num == parent[num]:
                return num
            parent[num] = find(parent[num])
            return parent[num]

        def union(x: int, y: int):
            parent[find(x)] = find(y)

        row = len(isConnected)
        self.count = (1 + row) * row // 2
        parent = list(range(row))
        for i in range(row):
            for j in range(i + 1, row):
                if isConnected[i][j] == 1:  # 城市相连，直接合并，不需要额外判断是否父节点一样
                    union(i, j)
                    self.count -= 1
        return sum(parent[i] == i for i in range(row))


if __name__ == '__main__':
    isConnected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    sol = Solution()
    print(sol.findCircleNum(isConnected))
