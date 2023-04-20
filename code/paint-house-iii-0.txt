#define min(a, b) a < b ? a : b
int minCost(int* houses, int housesSize, int** cost, int costSize, int* costColSize, int m, int n, int target){
    int dp[m][n][target+1];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                for(int k=1;k<=target;k++)
            {
                    dp[i][j][k] = INT_MAX; // it means not possible to achive this state
                    if(i==0)             //base case
                    {
                       if(k == 1)
                       {
                           if(houses[i] == 0)
                           dp[i][j][k] = cost[i][j];
                           else
                           if(houses[i] != 0 && houses[i]-1 == j)
                           dp[i][j][k] = 0;
                       }
                       continue;
                        
                    }
                if(houses[i] != 0)  // if already painted
                {
                    
                    if(houses[i]-1 == j)
                    {
                    dp[i][j][k]= dp[i-1][j][k];
                    for(int l=0;l<n;l++)
                    if(l != j && k > 1)
                    dp[i][j][k] = min(dp[i-1][l][k-1],dp[i][j][k]);
                    }
                }
                else
                {
                dp[i][j][k] =  dp[i-1][j][k] != INT_MAX?dp[i-1][j][k]+cost[i][j]:INT_MAX;
                    for(int l=0;l<n;l++)
                    {
                     if(k > 1 && l != j && dp[i-1][l][k-1] != INT_MAX)
                    dp[i][j][k] = min(dp[i-1][l][k-1]+cost[i][j],dp[i][j][k]);
                    } 
                }
            }
            
        }
    }
        int mi = INT_MAX;
    for(int i=0;i<n;i++)
        mi = min(mi,dp[m-1][i][target]);
    return mi == INT_MAX?-1:mi;
}