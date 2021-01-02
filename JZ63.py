# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # small top heap
        self.temp = []

    def _swap(self, i, j):
        if not (0 <= i < len(self.temp) and 0 <= j < len(self.temp)):
            raise IndexError("Index our of range!")
        if not i == j:
            store = self.temp[i]
            self.temp[i] = self.temp[j]
            self.temp[j] = store

    def Insert(self, num):
        # write code here
        self.temp.append(num)
        if len(self.temp) > 1:
            idx = len(self.temp) - 1  # track the index of inserted num
            while idx:
                if self.temp[idx] < self.temp[idx-1]:
                    self._swap(i=idx, j=idx-1)
                    idx -= 1
                else:
                    break

    def GetMedian(self):
        # write code here
        length = len(self.temp)
        if length % 2:  # odd
            return self.temp[int(length/2)]
        else:  # even
            return (self.temp[int(length/2)-1] + self.temp[int(length/2)])/2


if __name__ == '__main__':
    flow = [5,2,3,4,1,6,7,0,8]
    solution = Solution()
    for num in flow:
        solution.Insert(num=num)
        print(solution.GetMedian())
