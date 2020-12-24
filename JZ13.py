class Solution:
    def reOrderArray(self, array):
        # write code here
        array_odd = []
        array_even = []
        if not len(array):
            return []
        for num in array:
            if num % 2:
                array_odd.append(num)
            else:
                array_even.append(num)
        return array_odd + array_even


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    print(Solution().reOrderArray(array))
