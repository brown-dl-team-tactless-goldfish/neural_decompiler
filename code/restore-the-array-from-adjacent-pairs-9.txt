class Solution {
    void dfs(int node, unordered_map<int, vector<int>> &m, unordered_set<int> &vis, vector<int> &ans) {
        vis.insert(node);
        ans.push_back(node);
        for(int ad : m[node]) {
            if(vis.find(ad) == vis.end()) dfs(ad, m, vis, ans);
        }
    }

public:
    vector<int> restoreArray(vector<vector<int>>& ap) {
        unordered_map<int, vector<int>> m;
        for(auto e : ap) m[e[0]].push_back(e[1]), m[e[1]].push_back(e[0]);

        int start;
        for(auto i : m){
            if(i.second.size() == 1) {
                start = i.first;
                break;
            }
        }

        vector<int> ans;
        unordered_set<int> vis;
        dfs(start, m, vis, ans);

        return ans;
    }
};