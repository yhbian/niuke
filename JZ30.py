# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [array[0]]
        m = dp[0]
        for i in range(1, len(array)):
            if dp[i-1] <= 0:
                dp.append(array[i])
            else:
                dp.append(array[i]+dp[i-1])
            if dp[-1] > m:
                m = dp[-1]
        return m


if __name__ == '__main__':
    array = [1,-2,3,10,-4,7,2,-5]
    print(Solution().FindGreatestSumOfSubArray(array=array))
