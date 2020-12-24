class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = bin(n)[3:]
            for i in range(32-len(n)):
                n = '0' + n
            inv = ''
            for item in n:
                if item == '1':
                    inv += '0'
                else:
                    inv += '1'
            n = int(inv, 2) + 1
            n = bin(n)[2:]
        else:
            n = bin(n)[2:]
        c = map(int, n)
        return sum(list(c))


if __name__ == '__main__':
    solution = Solution()
    result = solution.NumberOf1(n=0)
    print(result)
