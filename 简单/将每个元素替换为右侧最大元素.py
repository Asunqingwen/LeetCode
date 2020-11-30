'''
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

完成所有替换操作后，请你返回这个数组。

 

示例：

输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]
 

提示：

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            arr[i], max_ = max_, max(arr[i], max_)
        return arr


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    sol = Solution()
    print(sol.replaceElements(arr))
