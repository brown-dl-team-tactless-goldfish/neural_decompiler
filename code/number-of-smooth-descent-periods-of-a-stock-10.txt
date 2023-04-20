class Solution {
public:
    long long getDescentPeriods(vector<int>& p) {
       long long ans=0;
        long long n=p.size();
        long long j=0;
        if(n==0)
        return 0;
        if(n==1)
        return 1;
        for(long long i=1;i<n;i++)
        {
            if(p[i-1]-p[i]==1)
            {
                j++;
            }else{
                ans+=(j+1)*j/2;
                j=0;
            }
        }
        
        ans+=(j+1)*j/2;
        return ans+n;
    }
};