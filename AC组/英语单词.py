"""
随机生成10个长度为6以内的英语单词字符串并添加到数组内，判断哪些字符串不包含标准键盘中第二行的键符，即：【a,s,d,f,g,h,j,k,l】，返回满足条件数组下标，该算法时间复杂度必须为O(n)
"""
from random import randint, choice
from typing import List


class Solution:
    def __init__(self):
        self.words = []
        self.alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']

    def geneWords(self):
        for _ in range(10):
            word_len = randint(1, 6)
            word = ''.join(choice(self.alphas) for _ in range(word_len))
            self.words.append(word)
        print(self.words)

    def isWord(self) -> List:
        alpha = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        ans = []
        for i in range(len(self.words)):
            for ch in self.words[i]:
                if ch in alpha:
                    ans.append(i)
                    break
        return ans


if __name__ == '__main__':
    sol = Solution()
    sol.geneWords()
    result = sol.isWord()
    print(result)
