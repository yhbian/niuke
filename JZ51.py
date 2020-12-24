# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        from_start = []
        from_end = []
        B = []
        s, e = 1, 1
        for i in range(len(A)-1):
            s, e = s * A[i], e * A[-i-1]
            from_start.append(s)
            from_end.append(e)

        # first element
        B.append(from_end[-1])

        # intermediate element
        for i in range(len(A)-2):
            B.append(from_start[i] * from_end[len(A)-3-i])

        # last element
        B.append(from_start[-1])
        return B


if __name__ == '__main__':
    solution = Solution()
    solution.multiply([7, 2])
