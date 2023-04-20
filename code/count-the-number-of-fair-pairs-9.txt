
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(),nums.end());
        long long int ans = 0;
        for(int i = 0;i<nums.size();i++){
            int x = lower_bound(nums.begin()+i+1,nums.end(),lower-nums[i])-nums.begin()+i;
            int y = upper_bound(nums.begin()+i+1,nums.end(),upper-nums[i])-nums.begin()+i;
            ans += (y-x);
        }
        return ans;
    }
};