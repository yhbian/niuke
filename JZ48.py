# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        if num2 < num1:
            t = num1
            num1 = num2
            num2 = t
        num1 = bin(num1)[2:]
        num2 = bin(num2)[2:]
        last = 0
        s = ''


if __name__ == '__main__':
    solution = Solution()
    solution.Add(1, 2)
