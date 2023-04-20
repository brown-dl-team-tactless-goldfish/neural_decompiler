class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> mp;
        vector<vector<int>> ans;
        for(auto x: matches) {
            mp[x[0]] = 0;
            mp[x[1]] = 0;
        }
        for(auto x: matches) mp[x[1]]--;
        vector<int> v1, v2;
        for(auto x: mp) {
            if(x.second == 0) v1.push_back(x.first);
            if(x.second == -1) v2.push_back(x.first);
        }
        ans.push_back(v1);
        ans.push_back(v2);
        return ans;
    }
};