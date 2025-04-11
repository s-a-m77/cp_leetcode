class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 0:
            first_odd = low + 1
        else:
            first_odd = low
        if high % 2 == 0:
            last_odd = high - 1
        else:
            last_odd = high
        if first_odd > last_odd:
            return 0
        return (last_odd - first_odd) 
solution = Solution()
low = 3
high = 7
print(solution.countOdds(low, high)) 