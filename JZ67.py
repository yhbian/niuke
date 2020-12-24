# -*- coding:utf-8 -*-
class Solution:
    @staticmethod
    def _int(_float):
        if _float - int(_float) < 0.5:
            return int(_float)
        else:
            return int(_float) + 1

    def _max_mul(self, number, m):
        if m == 1:
            return number
        mul = 1
        element = self._int(_float=float(number)/m)
        i = 1
        while i * element < number and i < m:
            mul *= element
            i += 1
        rest = number - element * (i-1)
        return mul * rest

    def cutRope(self, number):
        # write code here
        max_mul = number
        for m in range(1, number):
            this_mul = self._max_mul(number, m)
            if max_mul < this_mul:
                max_mul = this_mul
        return max_mul


if __name__ == '__main__':
    number = 16
    print(Solution().cutRope(number=number))
