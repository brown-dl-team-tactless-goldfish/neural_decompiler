class Solution {
public:
   vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
    vector<vector<int>> ans(n), directChild(n);
    for(auto& e: edges) 
        directChild[e[0]].push_back(e[1]);
    for(int i = 0; i < n; i++)
        dfs(i, i, ans, directChild);
    return ans;
}
void dfs(int x, int curr, vector<vector<int>>& ans, vector<vector<int>>& directChild) {
    for (auto& ch: directChild[curr]) 
        if(ans[ch].size() == 0 || ans[ch].back() != x) {
            ans[ch].push_back(x);
            dfs(x, ch, ans, directChild);
        }
}
};