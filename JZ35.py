import time


class Solution_slow:
    def InversePairs(self, data):
        # write code here
        count = [0]
        if len(data) < 2:
            return count
        for i in range(1, len(data)):
            if data[i] < data[i-1]:
                new_add = count[-1] + i
            elif data[i] == data[i-1]:
                new_add = count[-1] + i - 1
            else:
                new_add = sum([num > data[i] for num in data[:i-1]])
            count.append(count[-1]+new_add)
        return count[-1] % 1000000007


class Solution:
    def __init__(self):
        self.count = 0

    def merge(self, list1, list2):
        idx1, idx2 = 0, 0
        merged = []
        while idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1] <= list2[idx2]:
                merged.append(list1[idx1])
                idx1 += 1
            else:
                merged.append(list2[idx2])
                idx2 += 1
                self.count += len(list1)-idx1
        if idx1 < len(list1):
            for i in range(idx1, len(list1)):
                merged.append(list1[i])
        else:
            for i in range(idx2, len(list2)):
                merged.append(list2[i])
        return merged

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        list1, list2 = data[:len(data) // 2], data[len(data) // 2:]
        sorted1 = self.merge_sort(list1)
        sorted2 = self.merge_sort(list2)
        return self.merge(sorted1, sorted2)

    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        self.merge_sort(data)
        return self.count % 1000000007


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 0, 3, 4, 9, 6, 1, 4]
    # data = []
    print(Solution().InversePairs(data))
