# -*- coding:utf-8 -*-
import copy


class Solution:
    @staticmethod
    def _sum(lst):
        all_sum = ''
        for s in lst:
            all_sum += s
        return all_sum

    def _update(self, sorted_lst, new_entry):
        init = copy.copy(sorted_lst)
        init.append(new_entry)
        min_sum = self._sum(init)
        best_lst = init
        for idx in range(len(sorted_lst)+1):
            new_lst = copy.copy(sorted_lst)
            new_lst.insert(idx, new_entry)
            if self._sum(new_lst) < min_sum:
                best_lst = new_lst
                min_sum = self._sum(best_lst)
        return best_lst

    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = [str(num) for num in numbers]
        if len(numbers) == 1:
            return numbers[0]
        sorted_lst = [numbers[0]]
        for new in range(1, len(numbers)):
            sorted_lst = self._update(sorted_lst=sorted_lst, new_entry=numbers[new])
        return self._sum(sorted_lst)


if __name__ == '__main__':
    numbers = [3, 32, 321]
    print(Solution().PrintMinNumber(numbers=numbers))
