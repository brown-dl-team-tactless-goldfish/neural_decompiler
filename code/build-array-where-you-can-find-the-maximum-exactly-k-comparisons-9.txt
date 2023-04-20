#define ll long long int
int mod=1000000007;
class Solution {
public:
    int m;
    int dp[51][101][51];
    ll build(int n,int _max,int k)
    {
        if(n==0)
            return k==0;
        if(dp[n][_max][k]!=-1)
            return dp[n][_max][k];
        ll res=0;
        for(int i=1;i<=m;i++)
        {
            if(i>_max && k>0)
            {
                res=(res+build(n-1,i,k-1))%mod;
            }
            else if(i<=_max)
            {
                res=(res+build(n-1,_max,k))%mod;
            }
        }
        return dp[n][_max][k]=res;
    }
    int numOfArrays(int n, int M, int k) 
    {
        m=M;
        memset(dp,-1,sizeof(dp));
        return build(n,0,k)%mod;
    }
};