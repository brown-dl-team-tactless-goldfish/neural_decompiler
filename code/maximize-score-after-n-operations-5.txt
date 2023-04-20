class Solution {
public:
    int maxScore(vector<int>& A) {
        int N = A.size();
        int memo[8][1 << 14]{};
        function<int(int, int)> dfs = [&](int mask, int idx)->int {
            if(mask == ((1 << N)-1)) return 0;
            int& res = memo[idx][mask];
            if(res) return res;
            for(int i = 0; i < N; i++) {
                for(int j = i+1; j < N; j++) {
                    if(!((mask >> i)&1) && !((mask >> j)&1)) res = max(res, idx*gcd(A[i], A[j]) + dfs(mask | (1 << i) | (1 << j), idx+1));
                }
            }
            return res;
        };
        return dfs(0, 1);
    }
};