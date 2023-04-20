class Solution {
public:
    int countHillValley(vector<int>& nums) {
        if(nums.size()<3)
        {
            return 0;
        }
        int ans=0;
        for(int i=1;i<nums.size()-1;)
        {
            int num=nums[i];
            int idx1=i+1;
            int idx2=i-1;
            while(idx1<nums.size() and nums[idx1]==num)
            {
                idx1++;
            }
            while(idx2>0 and nums[idx2]==num)
            {
                idx2--;
            }
            if(idx1==nums.size() || idx2<0)
            {
                break;
            }
            if((nums[i]<nums[idx1] and nums[i]<nums[idx2]) || (nums[i]>nums[idx1] and nums[i]>nums[idx2]))
            {
                ans++;
            }
            i=idx1;
        }
        return ans;
    }
};