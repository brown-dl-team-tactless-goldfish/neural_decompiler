class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        m1 = [0]*101
        for i in nums:
            m1[i] += 1
        couple,single = 0,0
        for i in m1:
            if i%2:
                single += 1
            couple += i//2
        return [couple,single]
            