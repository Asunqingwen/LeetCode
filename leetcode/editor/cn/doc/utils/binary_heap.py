'''
二叉堆排序 binary heap
优先级队列 priority queue
'''


class MaxPQ:
    def __init__(self, cap):
        self._cap = cap
        # 索引0不用
        self._pq = [0] * (cap + 1)

    def __parent(self, node):
        return node // 2

    def __left(self, node):
        return node * 2

    def __right(self, node):
        return node * 2 + 1

    def isEmpty(self):
        return self._cap == 0

    # 返回最大值
    def max(self):
        return self._pq[1]

    # 删除最大值
    def delMax(self):
        max_value = self.max()
        # 最大元素换到最后
        self.__exchange(1, self._cap)
        self._pq.pop()
        self._cap -= 1
        self.__sink(1)
        return max_value

    # 插入
    def insert(self, node):
        self._cap += 1
        self._pq.append(node)
        self.__swim(node)

    # 上浮
    def __swim(self, k):
        parent_node = self.__parent(k)
        while (k > 1 and self.__compare(parent_node, k)):
            self.__exchange(parent_node, k)
            k = parent_node

    # 下沉，因为是完全二叉树，所以有左必有右
    def __sink(self, k):
        left_node = self.__left(k)
        right_node = self.__right(k)
        while left_node <= self._cap:
            max_node = left_node
            if right_node <= self._cap and self.__compare(max_node, right_node):
                max_node = right_node
            # 父节点最大，无需下沉
            if self.__compare(max_node, k):
                break
            self.__exchange(k, max_node)
            k = max_node

    # 交换
    def __exchange(self, i, j):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]

    # 对比，是否需要交换
    def __compare(self, i, j):
        return self._pq[i] < self._pq[j]
