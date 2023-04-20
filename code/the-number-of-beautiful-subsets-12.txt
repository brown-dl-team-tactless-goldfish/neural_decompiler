class Solution {
public:
    // DFS Helper for recursing through list building a unique subset
    void dfs(vector<int> &nums, int idx, int k, unordered_map<int, int> &mp, int &ans) {
        // If we have reached the end of the list, count this unique subset
        if(idx == nums.size()) ans++;
        else {
            // Otherwise, we need to recurse, if possible recurse taking this element for the subset
            if(!mp[nums[idx] - k] && !mp[nums[idx] + k]) {
                mp[nums[idx]]++;
                dfs(nums, idx + 1, k, mp, ans);
                mp[nums[idx]]--;
            }
            // Recurse without taking this element in the subset
            dfs(nums, idx + 1, k, mp, ans);
        }
    }
    
    // O(2^N) Solution that generates all valid subsets and counts them in the result variable
    int beautifulSubsets(vector<int>& nums, int k) {
        // Initialize our result as 0
        int ans = 0;
        // Initialize a map for the count of elements in our current set
        unordered_map<int, int> mp;
        // DFS through the numbers array from index 0
        dfs(nums, 0, k, mp, ans);
        // Return all of the counted sets - 1 for the empty set
        return ans - 1;
    }
};