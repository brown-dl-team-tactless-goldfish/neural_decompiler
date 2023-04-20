int dp[501][501];
class Solution {
public:
    int solve(int s, int e, vector<int> &v)
    {
        if(s>e)
        return 0;
        if(dp[s][e] != -1)
        return dp[s][e];
        int r = 0;
        for(int i=s; i<=e; i++)
        {
            r += v[i];
        }
        int l = 0;
        int ans = 0;
        for(int i = s; i<e; i++)
        {
            l += v[i];
            r -= v[i];
            if(l<r)
            ans = max(ans, l+solve(s, i, v));
            if(l == r)
            ans = max(ans, l+max(solve(s, i, v), solve(i+1, e, v)));
            if(l>r)
            ans = max(ans, r+solve(i+1, e, v));
        }
        return dp[s][e] = ans;
    }
    int stoneGameV(vector<int>& s) {
        memset(dp, -1, sizeof(dp));
        int n = s.size();
        return solve(0, n-1, s);
    }
};