# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        r"""
        When construct the difference equation, taking care about repetition.
        In this problem:

        F(n-1) is trivial
        Though it seems that F(n-2) has two ways to reach n, however, one of it is cover in the F(n-1) case.

        In conclusion, when consider F(n-k), iff the step is in-decomposable, it participates in the calculation. 
        """
        dp = [1, 2, 3]
        if not number:
            return 0
        if number < 4:
            return dp[number-1]

        for i in range(3, number):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.rectCover(4))
