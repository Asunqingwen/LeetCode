"""
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

 

示例 1：

输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释：
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2：

输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
 

提示：

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。
"""
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        id_dict = {word: len(word) for word in words}
        for word in words:
            len_ = id_dict[word]
            i = 0
            while i < len_:
                if word[:i + 1] in id_dict:
                    i += 1
                    continue
                break
            if i < len_:
                del id_dict[word]
        ans = []
        max_long = max(id_dict.values())
        for key in id_dict.keys():
            if id_dict[key] == max_long:
                ans.append(key)
        ans.sort()
        return ans[0]


if __name__ == '__main__':
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    sol = Solution()
    print(sol.longestWord(words))
