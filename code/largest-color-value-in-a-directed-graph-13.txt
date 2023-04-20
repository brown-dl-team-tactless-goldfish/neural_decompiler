class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        if (edges.size() == 0)
            return 1;
        vector<vector<int>> adj(n);
        vector<int> outDegree(n,0);
        // populating the child to parent edges and outDegree of each node
        for (auto &e : edges) {
            adj[e[1]].push_back(e[0]);
            outDegree[e[0]]++;
        }
        vector<vector<int>> dp(n,vector<int>(26,0));
        int result = -1;
        queue<int> q;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (outDegree[i] == 0) {
                q.push(i);
                dp[i][colors[i]-'a']++;
                cnt++;
            }
        }
        
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int c = q.front(); q.pop();
                for (auto &p : adj[c]) {
                    outDegree[p]--;
                    for (int i = 0; i < 26; i++) {
                        dp[p][i] = max(dp[p][i],dp[c][i]);
                    }
                    // once we found new OutDegree 0 we find the max
                    // result and increment self count
                    if (outDegree[p] == 0) {
                        dp[p][colors[p]-'a']++;
                        int m = *max_element(begin(dp[p]),end(dp[p]));
                        result = max(result,m);
                        q.push(p);
                        cnt++;
                    }
                }
            }
        }
        // there is a cycle in the graph
        if (cnt != n)
            return -1;
        return result;
    }
};