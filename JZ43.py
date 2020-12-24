class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not len(s):
            return ''
        if len(s) < n:
            return s
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = 'me'
    print(Solution().LeftRotateString(s, n=3))
