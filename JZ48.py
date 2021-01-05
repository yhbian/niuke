# -*- coding:utf-8 -*-
class PositiveSolution:  # This solution
    def Add(self, num1, num2):
        # write code here
        if not num2:
            return num1
        return self.Add(num1 ^ num2, (num1 & num2) << 1)


class Solution:
    def completion(self, num):
        # F = 16 = 2 ** 4
        return num & 0xFFFFFFFF

    def regularize(self, num):
        if num <= 0x7FFFFFFF:
            return num
        else:
            return ~(num ^ 0xFFFFFFFF)

    def Add(self, num1, num2):
        while num2:
            num1, num2 = self.completion(num1), self.completion(num2)
            num1, num2 = num1 ^ num2, (num1 & num2) << 1
        return self.regularize(num1)


# class Solution:
#     def Add(self, a, b):
#         while(b):
#            a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
#         return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)


if __name__ == '__main__':
    solution = Solution()
    print(solution.Add(1, -2))
