'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
'''
from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储有向图
        edges = defaultdict(list)
        # 存储每个节点的入度
        indegree = [0] * numCourses
        # 存储答案
        visited = 0

        for prerequisite in prerequisites:
            edges[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        # 将所有入度为0的节点放入队列
        q = deque([u for u in range(numCourses) if indegree[u] == 0])
        while q:
            # 从队首取一个节点
            u = q.popleft()
            # 放入答案
            visited += 1
            for v in edges[u]:
                indegree[v] -= 1
                # 如果v的入度为0，说明可以选修了
                if indegree[v] == 0:
                    q.append(v)
        return visited == numCourses


if __name__ == '__main__':
    numCourses = 5
    prerequisites = [[1, 0], [2, 0]]
    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))
