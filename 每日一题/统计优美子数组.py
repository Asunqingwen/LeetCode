"""
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 奇数下标保存
        odd = [i for i in range(len(nums)) if nums[i] % 2]
        # 第一个奇数坐标到第0个数之间都是偶数，最后一个奇数坐标到最后一个数之间都是偶数
        new_odd = [-1] + odd + [len(nums)]
        result = 0
        for i in range(len(odd) - k + 1):
            start = new_odd[i + 1] - new_odd[i]
            end = new_odd[i + k + 1] - new_odd[i + k]
            result += start * end
        return result


if __name__ == '__main__':
    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2]
    k = 2
    sol = Solution()
    result = sol.numberOfSubarrays(nums, k)
    print(result)
