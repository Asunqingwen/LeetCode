"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        # 初始化小顶堆
        heapify(nums)
        # 删除n-k个较小的元素，堆顶就是第K大的元素
        for n in nums[k:]:
            heappush(heap, n)
            heappop(heap)
        return heappop(heap)


if __name__ == '__main__':
    nums = [3, 7, 16, 10, 12, 13, 17, 23, 35, 1, 2, 12, 5]
    k = 2
    sol = Solution()
    result = sol.findKthLargest(nums, k)
    print(result)
