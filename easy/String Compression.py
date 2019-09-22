# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 0012 10:52
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: String Compression.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""
from typing import List


def compress(chars: List[str]) -> int:
    p1 = 0
    p2 = 0
    count = 0
    while p2 < len(chars):
        if chars[p2] == chars[p1]:
            count += 1
        else:
            if count > 1:
                res = []
                while count != 0:
                    res.append(count % 10)
                    count //= 10
                for i in range(len(res) - 1, -1, -1):
                    p1 += 1
                    chars[p1] = str(res[i])
            p1 += 1
            count = 1
            chars[p1] = chars[p2]
        p2 += 1
    if count > 0:
        if count > 1:
            res = []
            while count != 0:
                res.append(count % 10)
                count //= 10
            for i in range(len(res) - 1, -1, -1):
                p1 += 1
                chars[p1] = str(res[i])
        p1 += 1
    return p1


if __name__ == '__main__':
    input = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result = compress(input)
    print(result)
    print(input)
