'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
'''
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        num = (target + 1) // 2
        if num < 2:
            return []
        if (num + 1) * num // 2 == target:
            return [[i for i in range(1, num + 1)]]
        res = []
        left, right = 1, 2
        sum_ = 3
        while left < right and right <= num:
            if sum_ > target:
                sum_ -= left
                left += 1
            else:
                if sum_ == target:
                    res.append([i for i in range(left, right + 1)])
                right += 1
                sum_ += right

        return res


if __name__ == '__main__':
    target = 9
    sol = Solution()
    print(sol.findContinuousSequence(target))
