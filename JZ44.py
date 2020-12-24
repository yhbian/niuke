# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_list = s.split(' ')
        new_s = ''
        for i in range(len(s_list)):
            if i == len(s_list) - 1:
                new_s += s_list[-i-1]
            else:
                new_s += s_list[-i-1] + ' '
        return new_s


if __name__ == '__main__':
    s = 'student. a am I'
    solution = Solution()
    s = solution.ReverseSentence(s=s)
    print(s)
