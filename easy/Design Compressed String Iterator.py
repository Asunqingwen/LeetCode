# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 0012 14:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Design Compressed String Iterator.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
"""


class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.index = 0
        self.size = len(compressedString)
        self.count_len = 0
        self.count = 0
        self.flag = True

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        char = self.compressedString[self.index]
        ans = self.index + 1
        if self.flag:
            while ans < self.size and self.compressedString[ans].isnumeric():
                self.count = self.count * 10 + int(self.compressedString[ans])
                ans += 1
                self.count_len += 1
            self.flag = False
        self.count -= 1
        if self.count == 0:
            self.index += self.count_len + 1
            self.count_len = 0
            self.flag = True
        return char

    def hasNext(self) -> bool:
        return self.size != self.index


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
if __name__ == '__main__':
    obj = StringIterator("x6")
    param_1 = obj.next()
    param_2 = obj.next()
    param_3 = obj.next()
    param_4 = obj.next()
    param_5 = obj.next()
    param_6 = obj.next()
    print(param_3, param_4)
