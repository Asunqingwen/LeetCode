'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
'''
from typing import List
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(arr))
        return res


if __name__ == '__main__':
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    k = 8
    sol = Solution()
    print(sol.getLeastNumbers(arr, k))
