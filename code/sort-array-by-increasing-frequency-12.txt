class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return sorted(nums, key = lambda n: (cnt[n], -n))