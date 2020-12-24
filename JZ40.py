# -*- coding:utf-8 -*-
class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        count = {}
        for num in array:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        result = []
        for key, value in count.items():
            if value == 1:
                result.append(key)
        return result


if __name__ == '__main__':
    array = [1, 1, 2, 3, 3, 4, 4, 5, 6, 6]
    print(Solution().FindNumsAppearOnce(array=array))
