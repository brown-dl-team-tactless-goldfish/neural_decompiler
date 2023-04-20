class Solution {
public:
    int uf[112345];
    
    int find(int x) {
        return uf[x] != x ? (uf[x] = find(uf[x])) : x;
    }
    
    void join(int x, int y) {
        uf[find(x)] = find(y);
    }
    
    bool is_connected(int x, int y) {
        return find(x) == find(y);
    }
    
    vector<bool> distanceLimitedPathsExist(
            int n, 
            vector<vector<int>>& edges, 
            vector<vector<int>>& queries) {
        iota(uf, uf + n, 0);
        
        for (int i = 0; i < queries.size(); i++) {
            queries[i].push_back(i);
        }
        
        auto by_weight = [](auto &a, auto &b) {
            return a[2] < b[2];
        };
        
        sort(queries.begin(), queries.end(), by_weight);
        sort(edges.begin(), edges.end(), by_weight);
        
        vector<bool> ans(queries.size());
        int j = 0;
        for (auto &q : queries) {
            for (; j < edges.size() && edges[j][2] < q[2]; j++) {
                join(edges[j][0], edges[j][1]);
            }
            ans[q[3]] = is_connected(q[0], q[1]);
        }
        
        return ans;
    }
};