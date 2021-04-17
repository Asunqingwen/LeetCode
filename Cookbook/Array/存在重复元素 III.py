'''
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。

 

示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
 

提示：

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1
'''
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_len = t + 1  # 每个桶的范围
        bucket = dict()

        for i, num in enumerate(nums):
            ID = num // bucket_len  # python3向左取整
            if ID in bucket:  # 已经有桶，满足条件
                return True
            if (ID - 1) in bucket and num - bucket[ID - 1] <= t:  # 相邻桶
                return True
            if (ID + 1) in bucket and bucket[ID + 1] - num <= t:  # 相邻桶
                return True
            bucket[ID] = num
            if i >= k:  # 下一个元素的索引之差最大要超过k了，所以删除k范围内第一个元素所在的桶
                del bucket[nums[i - k] // (t + 1)]
        return False


if __name__ == '__main__':
    nums = [1, 5, 1, 9, 5, 9]
    k = 2
    t = 3
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate(nums, k, t))
