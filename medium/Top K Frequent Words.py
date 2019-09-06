# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 0006 22:03
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Top K Frequent Words.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    word_dict = {}
    count_dict = {}
    res = []
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    for key in word_dict.keys():
        if word_dict[key] in count_dict:
            count_dict[word_dict[key]].append(key)
        else:
            count_dict[word_dict[key]] = [key]
    count_dict = sorted(count_dict.items(), key=lambda x: x[0],reverse=True)
    for count in count_dict:
        count[1].sort()
        for c in count[1]:
            res.append(c)
            k -= 1
            if k <= 0:
                return res


if __name__ == '__main__':
    input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    result = topKFrequent(input, k)
    print(result)
