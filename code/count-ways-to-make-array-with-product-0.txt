primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        def nK(n: int, k: int) -> int:
            res = 1
            for p in primes:
                r = 0
                while k % p == 0:
                    r += 1
                    k /= p
                res *= comb(n - 1 + r, r)
            if (k != 1):
                res *= n            
            return res % 1000000007
        
        return [nK(n, k) for n, k in queries]     