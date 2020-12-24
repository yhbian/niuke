# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.candidate = []

    def FirstAppearingOnce(self):
        # write code here
        if not self.s:
            return '#'
        if not self.candidate:
            return '#'
        else:
            return self.candidate[0]

    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.candidate:
            self.candidate.append(char)
        else:
            self.candidate.remove(char)


if __name__ == '__main__':
    solution = Solution()
    solution.Insert(char='g')
    # solution.Insert(char='o')
    # solution.Insert(char='o')
    # solution.Insert(char='g')
    # solution.Insert(char='l')
    print(solution.FirstAppearingOnce())
