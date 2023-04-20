class Solution {
public:
    #define ll long long
    int countWays(vector<vector<int>>& ranges) {
        sort(ranges.begin(),ranges.end());
        vector<ll> dp(ranges.size(),0);
        dp[0]=2;  //we can place the first interval in any group
        int maxi=ranges[0][1];
        for(int i=1;i<ranges.size();i++)
        {
            //if it overlaps with any of previous intervals then we have same ways
            if(ranges[i][0]<=maxi)
                dp[i]=dp[i-1];
            else
                dp[i]=2*dp[i-1];  //we can place current range in any group (2 ways)
            maxi=max(maxi,ranges[i][1]);
            dp[i]%=1000000007;
        }
        return dp[ranges.size()-1];
    }
};