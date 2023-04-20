struct TrieNode {
    TrieNode* child[2] = {};
    int go = 0; 
    void increase(int number, int d) {
        TrieNode* cur = this;
        for (int i = 17; i >= 0; --i) {
            int bit = (number >> i) & 1;
            if (cur->child[bit] == nullptr) cur->child[bit] = new TrieNode();
            cur = cur->child[bit];
            cur->go += d;
        }
    }
    int findMax(int number) {
        TrieNode* cur = this;
        int ans = 0;
        for (int i = 17; i >= 0; --i) {
            int bit = (number >> i) & 1;
            if (cur->child[1 - bit] != nullptr && cur->child[1 - bit]->go > 0) {
                cur = cur->child[1 - bit];
                ans |= (1 << i);
            } else cur = cur->child[bit];
        }
        return ans;
    }
};

class Solution { 
public:
    TrieNode trieRoot;
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& qs) {
        int n = parents.size(), m = qs.size(), root = -1;
        vector<vector<int>> graph(n);
        for (int i = 0; i < n; ++i)
            if (parents[i] == -1) root = i;
            else graph[parents[i]].push_back(i);
        vector<vector<pair<int, int>>> queryByNode(n);
        for (int i = 0; i < m; ++i)
            queryByNode[qs[i][0]].push_back(make_pair(qs[i][1], i)); 

        vector<int> ans(m);
        dfs(root, graph, queryByNode, ans);
        return ans;
    }
    void dfs(int u, vector<vector<int>>& graph, vector<vector<pair<int, int>>>& queryByNode, vector<int>& ans) {
        trieRoot.increase(u, 1);
        for (auto& p : queryByNode[u])
            ans[p.second] = trieRoot.findMax(p.first);
        for (int& v : graph[u])
            dfs(v, graph, queryByNode, ans);
        trieRoot.increase(u, -1);
    }
};