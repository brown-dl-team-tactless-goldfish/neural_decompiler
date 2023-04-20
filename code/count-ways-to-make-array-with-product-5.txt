int comb[10013][14] = { 1 }, mod = 1000000007;
int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
class Solution {
public:
vector<int> waysToFillArray(vector<vector<int>>& qs) {
    if (comb[1][1] == 0)
        for (int n = 1; n < 10013; ++n)
            for (int r = 0; r < 14; ++r)
                comb[n][r] = r == 0 ? 1 : (comb[n - 1][r - 1] + comb[n - 1][r]) % mod;
    vector<int> res(qs.size(), 1);
    for (auto i = 0; i < qs.size(); ++i) {
        int n = qs[i][0], k = qs[i][1];
        for (auto p : primes) {
            int r = 0;
            while (k % p == 0) {
                ++r;
                k /= p;
            }
            res[i] = (long)res[i] * comb[n - 1 + r][r] % mod;
        }
        if (k != 1)
            res[i] = (long)res[i] * n % mod;
    }
    return res;
}
};