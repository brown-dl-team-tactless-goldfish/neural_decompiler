class Solution {
public:
    long solve(vector<int>&nums,int t,int i,int n,vector<vector<long>>&dp){
        if(t==0) return 0;
        if(t<0 || i>=n) return INT_MAX;
        if(dp[i][t]!=-1) return dp[i][t];
        long c1 = 1+solve(nums,t-nums[i],i,n,dp);
        long c2 = solve(nums,t,i+1,n,dp);
        return dp[i][t] = min(c1,c2);
    }
    int minimumNumbers(int num, int k) {
        int x = k;
        vector<int>nums;
        while(x<=num){
            if(x!=0) nums.push_back(x);
            x = (10+x);
        }
        vector<vector<long>>dp(nums.size()+1,vector<long>(num+1,-1));
        int c = solve(nums,num,0,nums.size(),dp);
        return (c>=INT_MAX)?-1:c;
    }
};