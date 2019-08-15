# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 9:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Consecutive Numbers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
"""

"""
select distinct Num as Consecutive 
From (
	select Num,
		case 
			when @prev = Num then @count := @count + 1
			when (@prev := Num) is not null then @count := 1
		end as CNT
	from Logs,(select @prev := null,@count := null) as t
) as temp
where temp.CNT >= 3
"""
