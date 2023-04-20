class Solution {
public:
    static bool cmp( pair<int, int> &a, pair<int, int> &b ) {
        if(a.first == b.first) return a.second > b.second;
        return a.first < b.first;
}
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> mp;
        vector<pair<int, int>> v;
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++) {
            mp[nums[i]]++;
        }
        for(auto c : mp) {
            v.push_back({c.second, c.first});
        }
        sort(v.begin(), v.end(), cmp);
        for(int i = 0; i < v.size(); i++) { // 
            while(v[i].first) {
                ans.push_back(v[i].second);
                v[i].first--;
            }
        }
        
        return ans;
    }
};