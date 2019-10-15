# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 11:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Advantage Shuffle.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
from typing import List


def advantageCount(A: List[int], B: List[int]) -> List[int]:
	A.sort()
	tmp_B = sorted(B)
	if A[0] > tmp_B[-1] or A[-1] < tmp_B[0]:
		return A
	head_B, tail_B = 0, len(B) - 1
	head_A = 0
	ans = {}
	while head_A < len(A):
		if A[head_A] > tmp_B[head_B]:
			if tmp_B[head_B] in ans:
				ans[tmp_B[head_B]].append(A[head_A])
			else:
				ans[tmp_B[head_B]] = [A[head_A]]
			head_B += 1
		else:
			if tmp_B[tail_B] in ans:
				ans[tmp_B[tail_B]].append(A[head_A])
			else:
				ans[tmp_B[tail_B]] = [A[head_A]]
			tail_B -= 1
		head_A += 1
	res = []
	for b in B:
		if len(ans[b]) > 1:
			res.append(ans[b].pop())
		else:
			res.append(ans[b][0])
	return res

def advantageCount1(A: List[int], B: List[int]) -> List[int]:
	n = len(A)
	res = [0] * n
	A.sort()
	index = sorted(range(n), key=lambda x: B[x])
	B = [B[i] for i in index]
	low = 0
	high = n - 1
	for a in A:
		if a > B[low]:
			res[index[low]] = a
			low += 1
		else:
			res[index[high]] = a
			high -= 1
	return res


if __name__ == '__main__':
	A = [702548877, 517539349, 368538467, 401095871, 202361400, 100834629, 921353446, 640319799, 169849965, 803113144,
	     184725553, 662262282, 586645328, 796776393, 412254342]
	B = [955208010, 719087363, 449185801, 121068011, 258102300, 132348377, 521162482, 805854357, 742178978, 637074814,
	     426851452, 278464259, 803879150, 671211893, 663605201]
	result = advantageCount1(A, B)
	print(result)
