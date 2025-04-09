class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9

sol = Solution()

print(sol.addDigits(135)) 