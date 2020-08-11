"""
设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。

add 操作 -  对内部数据结构增加一个数。
find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。

示例 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
示例 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        sums = dict()
        for num in self.nums:
            if value - num in sums:
                return True
            sums[num] = 1
        return False


if __name__ == '__main__':
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print(obj.find(4))
    print(obj.find(7))
