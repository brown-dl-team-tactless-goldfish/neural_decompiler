class Solution {
public:
    bool check(vector<int>& nums) {
        int c = 0, n = nums.size();
        for(int i=0; i<n; i++){
            if(nums[i] > nums[(i+1) % n])
                c++;
        }
        return c <= 1;
    }
};