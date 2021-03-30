'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

 

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 104
-109 <= nums[i] <= 109
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(num: int):
            '''
            查找自己的帮主
            :param num:要查找帮主的人
            :return:
            '''
            if sets[num] == num:  # 如果帮派的帮主就是自身，直接返回
                return num
            sets[num] = find(sets[num])  # 父节点设为根节点，路径压缩
            return sets[num]  # 直接返回帮主

        sets = {num: num for num in nums}
        for num in nums:
            if num + 1 in sets:
                sets[num] = find(num + 1)
        res = 0
        for key in sets.keys():
            value = find(sets[key])
            res = max(res, value - key + 1)
        return res


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))
