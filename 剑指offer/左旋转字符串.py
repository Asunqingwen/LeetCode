class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        list_s = list(s)
        for _ in range(n):
            list_s.append(list_s.pop(0))
        # print(list_s)
        return ''.join(list_s)


if __name__ == '__main__':
    sol = Solution()
    s = "abcdefg"
    k = 2
    sol.reverseLeftWords(s, k)
