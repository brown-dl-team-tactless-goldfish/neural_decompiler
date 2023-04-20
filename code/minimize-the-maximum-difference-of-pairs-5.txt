class Solution {
    bool check(vector<int> &nums, int p, int mid) {
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] - nums[i - 1] <= mid) {
                p--; i++;
            }
        }
        return p <= 0;
    }
public:
    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(), nums.end());
        int low = 0, high = nums[nums.size() - 1] - nums[0], ans = high;
        while(low <= high) {
            int mid = low + (high - low) / 2;
            if(check(nums, p, mid)) {
                ans = min(ans, mid);
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};