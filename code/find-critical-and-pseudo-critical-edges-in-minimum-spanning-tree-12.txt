class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        vector<vector<int>> ans(2);
        int m = edges.size();
        for (int i = 0; i < m; ++i) edges[i].push_back(i);
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });
        int value = kruskal(n, edges);
        for (int i = 0; i < m; ++i) {
            if (kruskal(n, edges, i) > value) ans[0].push_back(edges[i][3]);
            else if (kruskal(n, edges, -1, i) == value) ans[1].push_back(edges[i][3]);
        }
        return ans;
    }
    int kruskal(int n, vector<vector<int>>& edges, int skip = -1, int include = -1) {
        vector<int> f(n);
        for (int i = 0; i < n; ++i) f[i] = i;
        function<int(int)> find = [&](int x) {
            return f[x] == x ? x : f[x] = find(f[x]);
        };
        int ans = 0, count = 0;
        if (include != -1) {
            auto& e = edges[include];
            ans += e[2];
            f[find(e[0])] = find(e[1]);
            ++count;
        }
        for (int i = 0; i < edges.size(); ++i) {
            if (i == skip) continue;
            auto& e = edges[i];
            int x = find(e[0]), y = find(e[1]);
            if (x != y) {
                f[x] = y;
                ans += e[2];
                if (++count == n - 1) break;
            }
        }
        return count == n - 1 ? ans : INT_MAX;
    }
};