# -*- coding:utf-8 -*-


class RecursionSolution:
    r"""
    I. About the 'return' in recursion

    1. a function computes first and then return.
    2. In recursion, function computes create new branch, i.e. add a new component under the functional stack
    3. Once recursion reaches end criterion, it returns to the k-1 function and jumps out of the functional stack
    4. Once the stack has only one function, it returns the value outside.

    II. Recursion v.s. Dynamic Programming

    1. The core of this problem is F(n) = F(n-1) + F(n-2)
    2. We can also solve it with a DP method, see Solution
    """
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.jumpFloor(number-1) + self.jumpFloor(number-2)


class DPSolution:
    r"""
    F(n) = F(n-1) + F(n-2)
    F(1) = 1
    F(2) = 2
    """
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        dp = [1, 2]
        for i in range(2, number):
            dp.append(dp[i-2] + dp[i-1])
        return dp[-1]


if __name__ == '__main__':
    solution1 = RecursionSolution()
    solution2 = DPSolution()
    print(solution1.jumpFloor(1))
    print(solution2.jumpFloor(1))
