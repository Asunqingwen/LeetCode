# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 0006 22:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Top K Frequent Elements.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        for k in count.keys():
            print((-count[k],k))
    return sorted(count.keys(), key=lambda x: (-count[x], x))[:k]


if __name__ == '__main__':
    nums = [1]
    k = 1
    result = topKFrequent(nums, k)
    print(result)
