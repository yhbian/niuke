# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s.split('.')) > 2 or len(s.split('+')) > 3 or len(s.split('-')) > 3 or len(s.split('e')) > 2 or len(s.split('E')) > 2:
            return False
        # split the num
        if s.find('e') != -1:
            if s.split('e')[-1].find('.') != -1:
                return False
            s = s.split('e')
        elif s.find('E') != -1:
            if s.split('E')[-1].find('.') != -1:
                return False
            s = s.split('E')
        else:
            try:
                x = float(s)
            except:
                return False
        if len(s) > 1 and (s[0] == '' or s[-1] == ''):
            return False
        if s[0].find('+') > 0 or s[-1].find('+') > 0 or s[0].find('-') > 0 or s[-1].find('-') > 0:
            return False
        return True


if __name__ == '__main__':
    s = "1a3.14"
    print(Solution().isNumeric(s=s))
