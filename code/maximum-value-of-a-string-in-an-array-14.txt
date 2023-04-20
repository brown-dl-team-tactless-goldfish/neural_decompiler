class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(x) if x.isdigit() else len(x) for x in strs)