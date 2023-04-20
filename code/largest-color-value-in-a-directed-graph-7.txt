class Solution {
public:
    int largestPathValue(string s, vector<vector<int>>& e) {
        unordered_set<char> validChar(s.begin(), s.end());
        vector<vector<int>> g(s.size());
        for (auto& v : e) g[v[0]].push_back(v[1]);
        int ans = 0;
        for (auto c : validChar){
            unordered_map<int,int> m;
            for (int i = 0; i < s.size(); ++i)
                if (m.find(i) == m.end()){
                    ans = max(ans, dfs(c, s, g, i, m));
                    if (m[INT_MAX]) return -1;
                }
        }
        return ans;
    }
    int dfs(char& color, string& s, vector<vector<int>>& g, int node,
            unordered_map<int,int>& m){
            if (m.find(node) != m.end())
                return m[node] == -1 ? m[INT_MAX] = 1 : m[node];
            m[node] = -1;
            int largest = 0;
            for (auto& n : g[node])
                largest = max(largest, dfs(color, s, g, n, m));
            return m[node] = largest + (s[node] == color);
    }
};