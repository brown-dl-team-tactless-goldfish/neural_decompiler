class Solution {
public:
    int dp[101][10005];
    int solve(int k,int n){
        if(n==0 or n==1)return n;
        if(k==1)return n;
        if(dp[k][n]!=-1){
            return dp[k][n];
        }
        int answer=INT_MAX;
        int start=1;
        int end=n;
        while(start<=end){
            int middle=(start+end)/2;
            int left=solve(k-1,middle-1);
            int right=solve(k,n-middle);
            int temp=1+max(left,right);
            if(left<right){
                start=middle+1;
            }
            else{
                end=middle-1;
            }
            answer=min(answer,temp);
        }
    return dp[k][n]=answer;
    }
    int superEggDrop(int k, int n) {
        memset(dp,-1,sizeof(dp));
        return solve(k,n);
    }
};