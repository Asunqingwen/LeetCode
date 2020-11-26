'''
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

 

示例 1：

输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
示例 2：

输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]
 

提示：

1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_ = len(arr)
        count = 0
        i = 0
        while i < len_:
            if arr[i] == 0:
                count += 1
            count += 1
            if count >= len_:
                break
            i += 1
        j = len_ - 1
        while j >= 0:
            if arr[i] != 0:
                arr[j] = arr[i]
            elif arr[i] == 0 and count > len_ and j == len_ - 1:
                arr[j] = arr[i]
            else:
                arr[j] = arr[j-1] = arr[i]
                j -= 1
            i -= 1
            j -= 1




if __name__ == '__main__':
    arr = [8, 4, 5, 0, 0, 0, 0, 7]
    sol = Solution()
    print(sol.duplicateZeros(arr))
