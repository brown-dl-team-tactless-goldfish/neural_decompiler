class Solution:
    def maximumGood(self, S):
        n, ans = len(S), 0
        def valid(cur):
            for i in range(n):
                if cur & 1 << n-1-i:
                    for j in range(n):
                        if S[i][j] != 2 and S[i][j] != bool(cur & 1 << n-1-j): return False
            return True
        return max(bin(i).count('1') if valid(i) else 0 for i in range(1 << n))