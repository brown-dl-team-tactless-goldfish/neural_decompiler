class Solution {
public:
	int f(int i,int diff,vector<int>& rods,int n,vector<vector<int>>& dp){
		if(i==n){
			if(!diff) return 0;
			return -1e9;
		}
		if(dp[i][5000+diff]!=-1) return dp[i][5000+diff];
		int op1=rods[i]+f(i+1,diff+rods[i],rods,n,dp);
		int op2=f(i+1,diff-rods[i],rods,n,dp);
		int op3=f(i+1,diff,rods,n,dp);
		return dp[i][5000+diff]=max(max(op1,op2),op3);
	}

	int tallestBillboard(vector<int>& rods) {
		int n=rods.size();
		vector<vector<int>> dp(n,vector<int>(10000,-1));
		return f(0,0,rods,n,dp);
	}
};