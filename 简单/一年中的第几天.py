'''
给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

 

示例 1：

输入：date = "2019-01-09"
输出：9
示例 2：

输入：date = "2019-02-10"
输出：41
示例 3：

输入：date = "2003-03-01"
输出：60
示例 4：

输入：date = "2004-03-01"
输出：61
 

提示：

date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字。
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。
'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split('-')
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = int(year), int(month), int(day)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days[2] += 1
        res = 0
        for i in range(1, month):
            res += days[i]
        return res + day


if __name__ == '__main__':
    date = "2016-02-29"
    sol = Solution()
    print(sol.dayOfYear(date))
