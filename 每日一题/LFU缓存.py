# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 0005 10:28
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: LFU缓存.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4
"""
from bisect import bisect_left, insort


class LFUCache:

    def __init__(self, capacity: int):
        self.cap, self.tick = capacity, 0  # 容量和计时
        self.his = []  # 元素形式为：(freq, tick, key)
        self.dic = {}  # 键值对形式为：key:[val, freq, tick]

    def get(self, key: int) -> int:
        if key not in self.dic:  # key不存在
            return -1
        self.tick += 1  # 计时
        val, freq, tick = self.dic[key]  # 取出值、频率和时间
        self.dic[key][1] += 1  # 将频率+1
        self.his.pop(bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
        insort(self.his, (freq + 1, self.tick, key))  # 将更新后的记录二分插入
        return val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        self.tick += 1
        if key in self.dic:
            _, freq, tick = self.dic[key]  # 取出频率和时间
            self.dic[key][:] = value, freq + 1, self.tick  # 更新值、频率和计时
            self.his.pop(bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
            insort(self.his, (freq + 1, self.tick, key))  # 将更新后的记录二分插入
        else:  # 无该记录
            self.dic[key] = [value, 1, self.tick]
            if len(self.his) == self.cap:  # history容量已满
                del self.dic[self.his.pop(0)[2]]  # 移除history首个元素即对应的键值对
            insort(self.his, (1, self.tick, key))  # 将新记录插入history


from collections import defaultdict, OrderedDict


class LFUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.order_dict = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1

        value, freq = self.cache_dict.get(key)
        self.order_dict[freq].pop(key)
        if not self.order_dict[freq]:
            self.order_dict.pop(freq)
        freq += 1
        self.cache_dict[key] = (value, freq)
        self.order_dict[freq][key] = ''

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache_dict:
            temp_value, freq = self.cache_dict.get(key)
            self.order_dict[freq].pop(key)
            if not self.order_dict[freq]:
                self.order_dict.pop(freq)
            freq += 1
            self.cache_dict[key] = (temp_value, freq)
            self.order_dict[freq][key] = ''
            self.cache_dict[key] = (value, freq)
            return

        if len(self.cache_dict) == self.capacity:
            min_freq = min(self.order_dict)
            del_key, _ = self.order_dict[min_freq].popitem(last=False)
            if not self.order_dict[min_freq]:
                self.order_dict.pop(min_freq)
            self.cache_dict.pop(del_key)

        self.cache_dict[key] = (value, 0)
        self.order_dict[0][key] = ''


if __name__ == '__main__':
    # Your LFUCache object will be instantiated and called as such:
    # obj = LFUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    cache = LFUCache1(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 返回1
    cache.put(3, 3)  # 去除key2
    print(cache.get(2))  # 返回-1，未找到key 2
    print(cache.get(3))  # 返回3
    cache.put(4, 4)  # 去除key 1
    print(cache.get(1))  # 返回-1 ，未找到key 1
    print(cache.get(3))
    print(cache.get(4))
