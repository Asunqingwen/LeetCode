# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 10:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Absolute Difference.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of distinct integers arr, find all pairs of elements in ascending order with the minimum absolute difference of any two elements.



Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""
from typing import List


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    if not arr:
        return []
    arr.sort()
    ans = {}
    for i in range(len(arr) - 1):
        index = arr[i + 1] - arr[i]
        if index in ans:
            ans[index].append([arr[i], arr[i + 1]])
        else:
            ans[index] = [[arr[i], arr[i + 1]]]
    minidex = sorted(ans)
    return ans[minidex[0]]


if __name__ == '__main__':
    arr = []
    result = minimumAbsDifference(arr)
    print(result)
