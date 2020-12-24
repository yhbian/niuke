# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not len(numbers):
            return 0
        count = {}
        for num in numbers:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        public_num = None
        amount = 0
        for key, value in count.items():
            if value > amount:
                amount = value
                public_num = key
        if amount > len(numbers)/2:
            return public_num
        else:
            return 0


if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution(numbers=[1,2,3,3]))
