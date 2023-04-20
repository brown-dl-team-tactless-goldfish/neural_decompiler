class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0 
        val = 2*sum(skill) // len(skill)
        freq = Counter(skill)
        for i, (k, v) in enumerate(freq.items()):
            if v != freq[val - k]: return -1 
            ans += k*(val-k)*v
        return ans // 2