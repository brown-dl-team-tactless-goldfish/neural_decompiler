class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int _p = -1; 
        int _q = -1; 
        int p_ = -1; 
        int q_ = -1; 
        long long ret = 0; 
        for(int i = 0;i<nums.size();i++) {
            if(nums[i] == minK) {
                p_ = i; 
            } else if(nums[i] < minK) {
                _p = i; 
            }
            if(nums[i] == maxK) {
                q_ = i; 
            } else if(nums[i] > maxK) {
                _q = i; 
            }
            int l = max(_p,_q);
            int r = min(p_,q_);
            ret += max(0, r - l);
        }
        return ret; 
    }
};