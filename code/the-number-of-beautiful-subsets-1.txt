class Solution {
    int dfs(int i, int n, vector<int> &v, vector<int> &nums, int k) {
        if(i == n) return 1;
        
        int notPick = dfs(i + 1, n, v, nums, k), pick = 0;
        int f = 0;
        for(int j : v) {
            if(abs(j - nums[i]) == k) {
                f = 1;
                break;
            }
        }
        if(!f) {
            v.push_back(nums[i]);
            pick = dfs(i + 1, n, v, nums, k);
            v.pop_back();
        }
        return pick + notPick;
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> v;
        return dfs(0, n, v, nums, k) - 1;
    }
};