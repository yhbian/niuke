# -*- coding:utf-8 -*-
import math


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not len(array):
            return []
        small, big = None, None
        multi = array[-1] * array[-1]
        print(math.floor(len(array)/2))
        for i in range(int(math.floor(len(array)/2))):
            now = array[i]
            j = 0
            while j < len(array):
                if now + array[j] < tsum:
                    j += 1
                    continue
                elif now + array[j] == tsum:
                    if now * array[j] < multi:
                        small, big = now, array[j]
                        multi = now * array[j]
                    break
                else:
                    break
        if small is not None:
            return [small, big]
        else:
            return []


if __name__ == '__main__':
    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # tsum = 12
    array = [1, 2, 4, 7, 11, 16]
    tsum = 10
    solution = Solution()
    print(solution.FindNumbersWithSum(array, tsum))
