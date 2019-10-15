# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 15:46
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Invalid Transactions.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
from typing import List


def invalidTransactions(transactions: List[str]) -> List[str]:
	res = []
	dict1 = {}
	for transaction in transactions:
		tmp = transaction.split(',')
		flag = False
		if tmp[0] not in dict1:
			dict1[tmp[0]] = [[tmp[1], tmp[2], tmp[3], False]]
		else:
			tmp_list = dict1[tmp[0]]
			for l in tmp_list:
				if abs(int(l[0]) - int(tmp[1])) <= 60 and l[2] != tmp[-1]:
					if not l[3]:
						res.append(','.join([tmp[0], l[0], l[1], l[2]]))
						l[3] = True
					flag = True
			dict1[tmp[0]].append([tmp[1], tmp[2], tmp[3], flag])
		if int(tmp[2]) > 1000 or flag:
			dict1[tmp[0]][-1][3] = True
			res.append(transaction)
	return res


if __name__ == '__main__':
	transactions = ["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona", "bob,820,596,bangkok",
	                "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"]
	result = invalidTransactions(transactions)
	print(result)
