import copy

class Solution_slow:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # TODO:
        n = 1
        if index == 1:
            return n
        while index-1:
            n += 1
            k = copy.copy(n)
            while 1:
                if not k % 2:
                    k = k/2
                if not k % 3:
                    k = k/3
                if not k % 5:
                    k = k/5
                if (k % 2) * (k % 3) * (k % 5):
                    if k == 1:
                        index -= 1
                    break
        return n


if __name__ == '__main__':
    solution = Solution()
    print(solution.GetUglyNumber_Solution(11))
