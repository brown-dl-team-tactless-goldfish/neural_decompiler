class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        int maxKey = 0;
        unordered_map<int, vector<int>> map;
        for (int r = nums.size() - 1; r >= 0; --r) { // The values from the bottom rows are the starting values of the diagonals.
            for (int c = 0; c < nums[r].size(); ++c) {
                map[r + c].push_back(nums[r][c]);
                maxKey = max(maxKey, r + c);
            }
        }
        vector<int> ans;
        for (int key = 0; key <= maxKey; ++key)
            for (int v : map[key]) ans.push_back(v);
        return ans;
    }
};