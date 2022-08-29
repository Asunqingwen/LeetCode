import time_costing
from math import ceil


def isPrime(num):
    for i in range(2, ceil(num ** .5)):
        # 有其他整除因子
        if num % i == 0:
            return False
    return True


@time_costing.timeCosting
def countPrimes(n):
    isPrim = [1] * n
    for i in range(2, ceil(n ** .5)):
        if isPrim[i]:
            # i的倍数不可能是素数
            for j in range(i * i, n, i):
                isPrim[j] = 0
    count = 0
    for i in range(2, n):
        if isPrim[i]:
            count += 1
    return count


if __name__ == '__main__':
    n = 10
    print(countPrimes(n))
