"""
实现一个函数，把字符串中的每个空格替换成”%#”，该算法时间复杂度必须为O(n)
输入：Hello World
输出：Hello%#World

输入：This is a Tree
输出：This%#is%#a%#Tree
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return '%#'.join(s.split(' '))


if __name__ == '__main__':
    s = "This is a Tree"
    sol = Solution()
    result = sol.replaceSpace(s)
    print(result)
