"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        # 数组长度为n+1，数字为1-n
        left, right = 1, length - 1
        result = -1
        while left <= right:
            # 当前数
            mid = left + (right - left) // 2
            cnt = 0
            for i in range(length):
                cnt += (nums[i] <= mid)
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                result = mid
        return result


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    result = sol.findDuplicate(nums)
    print(result)
