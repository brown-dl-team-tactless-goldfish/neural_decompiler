class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        max_val = 1
        for c in sorted(coins):
            if c > max_val:
                break
            max_val += c
        return max_val