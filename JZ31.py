class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for num in range(n):
            s = str(num+1)
            count += list(map(int, list(s))).count(1)
        return count


if __name__ == '__main__':
    n = 55
    print(Solution().NumberOf1Between1AndN_Solution(n))
