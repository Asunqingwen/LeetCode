"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
 

注意：

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second_row = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third_row = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        res = []
        for word in words:
            word_ = word.lower()
            i = 0
            while i < len(word_):
                if word_[i] not in first_row:
                    break
                i += 1
            if i == len(word_):
                res.append(word)
                continue
            elif i > 0:
                continue

            while i < len(word_):
                if word_[i] not in second_row:
                    break
                i += 1
            if i == len(word_):
                res.append(word)
                continue
            elif i > 0:
                continue

            while i < len(word_):
                if word_[i] not in third_row:
                    break
                i += 1
            if i == len(word_):
                res.append(word)
                continue
            elif i > 0:
                continue
        return res


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    sol = Solution()
    print(sol.findWords(words))
