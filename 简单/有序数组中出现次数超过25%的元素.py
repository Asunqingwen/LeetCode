'''
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数

 

示例：

输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6
 

提示：

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
'''
from typing import List
import bisect


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        len_ = len(arr)
        span = len_ // 4 + 1
        for i in range(0, len_, span):
            l = bisect.bisect_left(arr, arr[i])
            r = bisect.bisect_right(arr, arr[i])
            if r - l >= span:
                return arr[i]


if __name__ == '__main__':
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    sol = Solution()
    print(sol.findSpecialInteger(arr))
