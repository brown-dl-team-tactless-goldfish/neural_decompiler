class Solution {
public:
    int dp[501][170];
    int get(int i,int n,vector<int>& slices)
    {
        if(n==0 || i>=slices.size())
            return 0;
        if(dp[i][n]!=-1)
            return dp[i][n];
        return dp[i][n]=max(get(i+1,n,slices),slices[i]+get(i+2,n-1,slices));
    }
    int maxSizeSlices(vector<int>& slices) 
    {
        int n=slices.size();
        memset(dp,-1,sizeof(dp));
        
        //Case 1 ignore first element
        int p1=get(1,n/3,slices); 
        memset(dp,-1,sizeof(dp));
        
        //Case 2 ignore last element
        slices[n-1]=0;
        int p2=get(0,n/3,slices);
        return max(p1,p2);
    }
};