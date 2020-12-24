# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not len(s):
            return 0
        num = 0
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4':4, 
                    '5': 5, '6': 6, '7': 7, '8': 8, '9':9}
        syntax = None
        if s[0] == '+':
            s = s[1:]
            length = len(s)
            syntax = 1
        elif s[0] == '-':
            s = s[1:]
            length = len(s)
            syntax = -1
        else:
            length = len(s)
        multi = 10 ** (length-1)
        for i in range(length):
            if s[i] in num_dict.keys():
                num += num_dict[s[i]] * multi
            else:
                return 0
            multi = multi/10
        if syntax is not None:
            return int(num * syntax)
        else:
            return int(num)


if __name__ == '__main__':
    solution = Solution()
    s = '-123'
    print(solution.StrToInt(s))
