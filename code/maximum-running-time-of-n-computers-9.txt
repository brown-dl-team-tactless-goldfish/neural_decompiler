class Solution {
public:
    bool find(vector<int>&nums,long long c,long long mid)
    {
        long long total=mid*c;
        for(int i=0;i<nums.size();i++)
        {
            total-=min(1ll*nums[i],1ll*mid);
        }
        return total<=0;
    }
    long long maxRunTime(int n, vector<int>&nums) 
    {
        long long ans=0;
        long long l=0;
        long long r=accumulate(nums.begin(),nums.end(),0ll);
        while(l<=r)
        {
            long long mid=(l+r)/2;
            if(find(nums,n,mid))
            {
                ans=mid;
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }
        }
        return ans;
    }
};