from typing import List


def getDeng(n: int) -> int:
    dengs = [0] * (n + 1)
    for i in range(1, n + 1):
        tmp = i
        while tmp <= n:
            dengs[tmp] ^= 1
            tmp += i
    return sum(dengs)


if __name__ == '__main__':
    n = 100
    res = getDeng(100)
    print(res)
    # 孙庆文-20211129
