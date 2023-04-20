class Solution {
public:
    int longestArithSeqLength(vector<int>& A) {
        int n = A.size();
        if(n < 3) return n;
        vector<vector<int>> dp(n, vector<int>(n, 2));
        int out = 2;
        for(int i = 0; i < n; i++)
        {
            for(int j = i+1; j < n; j++)
            {
                int diff = A[j]-A[i];
                int curr = A[j] + diff;
                for(int k = j+1; k <n; k++)
                {
                    if(A[k] == curr)
                    {                    
                        dp[i][j]++;
                        curr = A[k]+diff;
                    }
                }
                out = std::max(out, dp[i][j]);
            }
        }
        return out;
    }
};