class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long ans = 0;
        bool minFound = false, maxFound = false;
        int start = 0, minStart = 0, maxStart = 0;
        for(int i=0; i<nums.size(); i++) {
            int num = nums[i];
            if(num < minK or num > maxK) {
                minFound = false;
                maxFound = false;
                start = i+1;
            }
            if(num == minK) {
                minFound = true;
                minStart = i;
            }
            if(num == maxK) {
                maxFound = true;
                maxStart = i;
            }
            if(minFound and maxFound) {
                ans += (min(minStart, maxStart) - start + 1);
            }
        }
        return ans;
    }
};