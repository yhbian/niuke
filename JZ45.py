# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not len(numbers):
            return False
        if len(numbers) == 1:
            return True

        numbers = sorted(numbers)
        if numbers[-1] == 0:
            return True
        count = 0  # num of 0
        while not numbers[0]:
            numbers.pop(0)
            count += 1
        if len(numbers) <= 1:
            return True
        derive = []
        for i in range(1, len(numbers)):
            derive.append(numbers[i] - numbers[i-1] - 1)
        if sum(derive) == count:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().IsContinuous(numbers=[0, 0, 0, 0, 0]))  # [1, 0, 0, 5, 0]
