class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n;
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3));   