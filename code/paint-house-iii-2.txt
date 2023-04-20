class Solution {
private:
    int dp[101][21][101];
    vector<int> h;
    vector<vector<int>> c;
    int m;
    int n;
    int target;
    int helper(int i, int prevColor, int nbrs)
    {
        if(nbrs>target)
            return INT_MAX/2;
        
        if(i==m)
            return nbrs==target?0:INT_MAX/2;
        if(dp[i][prevColor][nbrs]!=-1)
            return dp[i][prevColor][nbrs];
        
        int ans = INT_MAX;
        if(h[i]==0)
            for(int j=0;j<n;j++)
                ans = min(ans, c[i][j] + helper(i+1, j+1, (j+1==prevColor)?nbrs:nbrs+1));
        else 
            ans = min(ans, helper(i+1,h[i], (h[i]==prevColor)?nbrs:nbrs+1));
        
        dp[i][prevColor][nbrs]=ans;
        return ans;
    }
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int numHouses, int numColors, int t) {
        memset(dp,-1,sizeof(dp));
        h = houses;
        c = cost;
        m = numHouses;
        n = numColors;
        target = t;
        
        int ans = helper(0,0,0);
        return ans>=INT_MAX/2?-1:ans;
    }
};