# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        for start in range(1, tsum/2+1):
            sum = 0
            i = start
            while sum < tsum:
                sum += i
                i += 1
                if sum == tsum:
                    result.append(list(range(start, i)))
        return result


if __name__ == '__main__':
    tsum = 100
    print(Solution().FindContinuousSequence(tsum=tsum))
