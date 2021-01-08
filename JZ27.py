# -*- coding:utf-8 -*-
import time


class Solution:
    def __init__(self):
        self.lst = []

    def swap(self, s, i, j):
        if i == j:
            return s
        if i > j:
            i, j = j, i
        return s[:i] + s[j] + s[i:j] + s[j+1:]

    def _Permutation(self, ss, process=None):
        # write code here
        # process records the recursion step
        self.lst.append(ss)
        if not ss:
            return [""]
        if not process:
            process = 0
        # when the process goes to the end of the string, recursion stop
        if process == len(ss):
            return
        process += 1
        anchor = process - 1
        for i in range(anchor, len(ss)):
            next_str = self.swap(ss, anchor, i)
            self._Permutation(next_str, process)

    def Permutation(self, ss):
        self._Permutation(ss)
        return sorted(list(set(self.lst)))


if __name__ == '__main__':
    solution = Solution()
    s = "abcdefghi"
    time1 = time.time()
    solution.Permutation(s)
    print(time.time()-time1)
