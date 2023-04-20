class Solution {
public:
    const long long  mod=1e9+7;
    long long find(long long a,long long b)
    {
        long long res=1;
        while(b)
        {
            if(b&1)
            {
                res=(res*a)%mod;
            }
            a=(a*a)%mod;
            b=b>>1;
        }
        return res;
    }
    int countGoodNumbers(long long n) 
    {
        long long odd=n/2;
        long long ans=find(4,odd)%mod;
        ans=ans*find(5,n-odd);
        return ans%mod;
    }
};