class Solution {
public:
    int mod = 1e9 + 7;
    int dp[5001][4][4][4];
    int dfs(int row, int aO, int bO, int cO)
    {
        if(row == 0)return 1;
        if(dp[row][aO][bO][cO] != 0)return dp[row][aO][bO][cO];
        vector<int> colors = {1, 2, 3};
        int ans = 0;
        for(auto a : colors)
            if(a != aO)
                for(auto b: colors)
                    if(b != bO && a != b)
                        for(auto c : colors)
                            if(c != cO && b != c)
                                ans = (ans + dfs(row - 1, a, b, c))%mod;
        
        return dp[row][aO][bO][cO] = ans%mod;
    }
    int numOfWays(int n) {
        memset(dp, 0, sizeof(dp));
        return dfs(n, 0, 0, 0);
    }
};