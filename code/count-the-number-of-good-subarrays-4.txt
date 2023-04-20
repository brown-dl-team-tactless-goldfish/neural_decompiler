    def countGood(self, A: List[int], k: int) -> int:
        res = cur = i = 0
        count = Counter()
        for j in range(len(A)):
            k -= count[A[j]]
            count[A[j]] += 1
            while k <= 0:
                count[A[i]] -= 1
                k += count[A[i]]
                i += 1
            res += i
        return res