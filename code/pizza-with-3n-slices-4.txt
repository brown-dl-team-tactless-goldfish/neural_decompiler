class Solution {
public:
    int dp[505][2][170];
    int solve(vector<int>& slices, int st, int end,int type, int n){
        if(st > end) return 0;
        if(dp[st][type][n] != -1) return dp[st][type][n];
        int op1 = INT_MIN, op2 = INT_MIN;
        
        op1 = solve(slices, st + 1, end,type, n);
        if(n > 0)
            op2 = slices[st] + solve(slices, st + 2, end, type,n - 1);
        return dp[st][type][n] = max(op1, op2);
    }
    int maxSizeSlices(vector<int>& slices) {
        int len = slices.size();
        int n = len / 3;
        memset(dp, -1, sizeof(dp));
        return max(solve(slices, 0, len - 2,0, n), solve(slices, 1, len -1,1, n));
    }
};