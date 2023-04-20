class Solution {
public:
    int k;
    int n;
    int p[2001][2001];
    int memo[3000];
    int f(int idx)
    {
        if(idx>=n)
        {
            return 0;
        }
        if(memo[idx]!=-1)
        {
            return memo[idx];
        }
        int ans=0;
        for(int i=idx;i<n;i++)
        {
            if((i-idx+1>=k)&&p[idx][i])
            {
                ans=max(ans,1+f(i+1));
            }
        }
        ans=max(ans,f(idx+1));
        return memo[idx]=ans;
    }
    int maxPalindromes(string s, int K) 
    {
        k=K;
        memset(p,0,sizeof(p));
        memset(memo,-1,sizeof(memo));

        n=s.size();
        for(int gap=0;gap<n;gap++)
        {
            for(int i=0,j=gap;j<n;i++,j++)
            {
                if(gap==0)
                {
                    p[i][j]=1;
                }
                else if(gap==1)
                {
                    p[i][j]=(s[i]==s[j]);
                }
                else
                {
                    if(s[i]==s[j]&&p[i+1][j-1])
                    {
                        p[i][j]=1;
                    }
                }
                    
            }
        }     
        return f(0);
    }
};