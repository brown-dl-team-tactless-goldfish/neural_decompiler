class Solution {
public:
	vector<int> p;
	int n;
	vector<vector<int>> dp;
	int winDiff(int start, int m){
		if(start>=n) return 0;
		if(dp[start][m]>0) return dp[start][m];

		if(start+2*m>=n){
			int cur=0;
			for(int i=start;i<n;i++){
				cur+=p[i];
			}
			dp[start][m]=cur;
			return dp[start][m];
		}
		int tem=0;
		int ans=INT_MIN;
		for(int x=1;x<=2*m;x++){
			tem+=p[start+x-1];
			ans=max(ans,tem-winDiff(start+x,max(m,x)));
		}
		dp[start][m]=ans;
		return ans;

	}
	int stoneGameII(vector<int>& piles) {
		p=piles;
		n=piles.size();
		dp.assign(n+1,vector<int>(n+1));

		int tol=0;
		for(auto& x:piles){
			tol+=x;
		}
		return (tol+winDiff(0,1))/2;


	}
};