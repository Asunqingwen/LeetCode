'''
请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。

 

示例 1：

输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
示例 2：

输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15
 

提示：

给定的日期是 1971 年到 2100 年之间的有效日期。
'''


class Solution:
    def leap_year(self, year):
        return ((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0))

    def date_to_int(self, year, month, day):
        month_length = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ans = day - 1
        while month != 0:
            month -= 1
            ans += month_length[month]
            if month == 2 and self.leap_year(year):
                ans += 1
        ans += 365 * (year - 1971)
        ans += (year - 1) // 4 - 1971 // 4
        ans -= (year - 1) // 100 - 1971 // 100
        ans += (year - 1) // 400 - 1971 // 400
        return ans

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = [int(i) for i in date1.split('-')]
        date2 = [int(i) for i in date2.split('-')]
        return abs(self.date_to_int(*date1) - self.date_to_int(*date2))


if __name__ == '__main__':
    date1 = "2020-01-15"
    date2 = "2019-12-31"
    sol = Solution()
    print(sol.daysBetweenDates(date1, date2))
