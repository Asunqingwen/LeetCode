# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 9:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Exchange Seats.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
 

Mary wants to change seats for the adjacent students.
 

Can you write a SQL query to output the result for Mary?
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last one's seat.
"""
"""
select (
		case 
			when mod(id,2) = 1 and id = (select count(*) from seat) then id
			when mod(id,2) = 1 then id + 1
			else id - 1
		end) as id,student
from seat 
order by id;
"""