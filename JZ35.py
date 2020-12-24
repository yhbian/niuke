class Solution:
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


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    print(Solution().InversePairs(data))
