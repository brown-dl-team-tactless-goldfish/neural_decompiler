class Solution {
   public:
    int longestNiceSubarray(vector<int> &nums) {
        int n = nums.size();
        int res = 1, l = 0, r = 1;
        while (r < n) {
            int d = 32;
            bool flag = true;
            for (int k = r - 1; k >= l && d--; k--) {
                if (nums[k] & nums[r]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                res = max(res, r - l + 1);
                r++;
            } else {
                l++;
            }
        }
        return res;
    }
};