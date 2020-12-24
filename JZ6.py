class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not len(rotateArray):
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]


if __name__ == '__main__':
    rotateArray = []
    solution = Solution()
    result = solution.minNumberInRotateArray(rotateArray=rotateArray)
    print(result)
