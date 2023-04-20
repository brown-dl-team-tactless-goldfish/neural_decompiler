class Solution {
public:
    long long findScore(vector<int>& nums) {
        long long ans = 0, n = nums.size();
        vector<pair<int, int>> v;
        for(int i=0; i<n; i++) v.push_back({nums[i], i});
        
        sort(v.begin(), v.end());
        unordered_set<int> seen;
        
        for(auto i : v) {
            int val = i.first, idx = i.second;
            if(seen.find(idx) == seen.end()) {
                ans += val;
                seen.insert(idx);
                seen.insert(idx + 1);
                seen.insert(idx - 1);
            }
        }
        return ans;
    }
};