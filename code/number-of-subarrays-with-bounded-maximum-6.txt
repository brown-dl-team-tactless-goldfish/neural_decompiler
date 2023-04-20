class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int n = nums.size();
        int count = 0,ans = 0,c = 0;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] >= left && nums[i] <= right)
            {
                count++;
                count += c;
                c = 0;
            }
            else if (nums[i] < left)
            {
                c++;
            }
            else if (nums[i] > right)
            {
                count = 0;
                c = 0;
            }
            ans += count;
        }
        return ans;
    }
};