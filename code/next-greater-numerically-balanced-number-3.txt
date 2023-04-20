class Solution {
public:
    int nextBeautifulNumber(int n) 
    {
        int ans=n;
        auto find=[&](int num)
        {
            vector<int>dp(10,0);
            while(num)
            {
                dp[num%10]++;
                if(num%10==0)
                {
                    return false;
                }
                num=num/10;
            }
            for(int i=1;i<10;i++)
            {
                if(dp[i]&&dp[i]!=i)
                {
                    return false;
                }
            }
            return true;
        };
        for(;;)
        {
            ans++;
            if(find(ans))
            {
                break;
            }
           
        }
        return ans;
    }
};