# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not size:
            return []
        if len(num) < size:
            return []
        if size == 1:
            return num
        window = num[:size]
        dp = [max(window)]
        idx = 1
        while idx + size < len(num)+1:
            new_entry = num[idx + size - 1]
            window.append(new_entry)
            gone = window.pop(0)
            if new_entry > dp[-1]:
                dp.append(new_entry)
            elif new_entry < gone and dp[-1] != gone:
                dp.append(dp[-1])
            else:
                dp.append(max(window))
            idx += 1
        return dp


if __name__ == '__main__':
    num, size = [2, 3, 4, 2, 6, 2, 5, 1], 3
    print(Solution().maxInWindows(num=num, size=size))
