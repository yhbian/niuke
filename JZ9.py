# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        dp = [1, 1, 2]
        for i in range(2, number):
            dp.append(sum(dp))
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.jumpFloorII(3))
