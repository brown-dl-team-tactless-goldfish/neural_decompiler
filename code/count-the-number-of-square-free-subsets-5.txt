class Solution {
public:
    int squareFreeSubsets(vector<int>& nums) {
        int cnt[31] = {};
        for (int num: nums)
            ++cnt[num];
        int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        long dp[1024] = {1};
        int mod = 1e9 + 7;
        for (int num = 2; num <= 30; ++num) {
            if (cnt[num] == 0 || num % 4 == 0 || num % 9 == 0 || num % 25 == 0)
                continue;
            int mask = 0;
            for (int i = 0; i < 10; ++i) {
                if (num % primes[i] == 0)
                    mask |= (1 << i);
            }
            for (int i = 0; i < 1024; ++i) {
                if ((i & mask) == 0)
                    dp[i|mask] = (dp[i|mask] + cnt[num] * dp[i]) % mod;
            }
        }
        auto pow2 = [] (int n, int mod) {
            int ret = 1;
            long base = 2;
            while (n) {
                if (n & 1)
                    ret = ret * base % mod;
                base = base * base % mod;
                n >>= 1;
            }
            return ret;
        };
        return (reduce(dp, dp+1024, 0LL, [&] (auto sum, int x) {
            return (sum + x) % mod;
        }) * pow2(cnt[1], mod) - 1 + mod) % mod;
    }
};