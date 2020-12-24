# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not len(s):
            return -1
        candicate = {}
        blacklist = []
        for i, element in enumerate(s):
            if element in blacklist:
                continue
            elif element not in candicate.keys():
                candicate[element] = i
            else:
                candicate.pop(element)
                blacklist.append(element)
        if len(candicate):
            return min(list(candicate.values()))
        else:
            return -1


if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar(s="googgle"))
