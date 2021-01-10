# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def __init__(self):
         self.flag = 0

    def match(self, s, pattern):
        # write code here
        # end criterion
        if not pattern and s:
            return False

        if not pattern and not s:  # pattern == s == [], match ends
            self.flag += 1
            return True

        if len(pattern) == 1:
            if len(s) == 1 and (pattern == s or pattern == "."):
                self.flag += 1  # matched
                return True
            else:
                return False

        # matching ... with len(pattern) >= 2
        # Case 1: pattern[1] is not "*"
        if pattern[1] != "*":
            if not s:
                return False
            else:
                if pattern[0] == "." or pattern[0] == s[0]:  # matched
                    self.match(s[1:], pattern[1:])  # go on ...
                else:   # match failed
                    return False
        # Case 2: pattern[1] is "*", which means pattern[0] could repeat any times including 0
        else:
            if not s:
                self.match(s, pattern[2:])
            else:
                # Case 2.1 pattern[0] is not s[0], repeat 0 time, ignore pattern[0:2], matching s and pattern[2:]
                if pattern[0] != s[0] and pattern[0] != ".":
                    self.match(s, pattern[2:])
                # Case 2.2 pattern[0] matched s[0], ignore s[0] and matching s[:1] and pattern
                else:
                    self.match(s[1:], pattern)
                    self.match(s[1:], pattern[2:])
                    self.match(s, pattern[2:])

        return self.flag > 0


if __name__ == '__main__':
    s_ = ''
    pattern_ = '.*.*'
    print(Solution().match(s_, pattern_))
