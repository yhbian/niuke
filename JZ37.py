# -*- coding:utf-8 -*-
import math


class Solution1:
    def GetNumberOfK(self, data, k):
        # write code here
        if not len(data):
            return 0
        if (k < data[0]) or (k > data[-1]):
            return 0
        if data[0] == data[-1]:
            if data[0] == k:
                return len(data)
            else:
                return 0
        if data[0] == k:
            count = 0
            while data[count] == k:
                count += 1
            return count
        if data[-1] == k:
            count = 0
            while data[len(data) - count - 1] == k:
                count += 1
            return count
        pointer1 = 0
        pointer2 = len(data) - 1
        # rough location
        while 1:
            mid = int(math.floor((pointer1+pointer2)/2))
            if data[mid] > k:
                pointer2 = mid
                continue
            if data[mid] < k:
                pointer1 = mid
                continue
            if data[mid] == k:
                pointer1 = mid
                break
            if data[pointer2] == k:
                pointer1 = pointer2
                break

        left, right = 0, 0
        while data[pointer1-left] == k:
            left += 1
        while data[pointer1+right] == k:
            right += 1
        count = left + right - 1
        return count


class Solution2:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not len(data):
            return 0
        if len(data) == 1:
            if data[0] == k:
                return 1
            else:
                return 0
        left, right = 0, len(data) - 1
        while 1:
            if data[left] != k:
                left += 1
            if data[right] != k:
                right -= 1
            if data[left] == k and data[right] == k:
                return right - left + 1
            if left >= right:
                return 0


if __name__ == '__main__':
    print(Solution().GetNumberOfK(data=[3], k=3))
