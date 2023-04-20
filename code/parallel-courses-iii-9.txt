class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<int> g[n];
        int indeg[n], mx_time[n];
        memset(indeg,0,sizeof indeg);
        memset(mx_time,0,sizeof mx_time);
        for (auto edge:relations){
            g[edge[0]-1].push_back(edge[1]-1);
            indeg[edge[1]-1]++;
        }
        queue<int> q;
        for (int i=0;i<n;i++){
            if (!indeg[i]) q.push(i);
        }
        while (q.size()>0){
            int node = q.front(); q.pop();
            for (auto neighbour: g[node]){
                indeg[neighbour]--;
                if (indeg[neighbour]==0) q.push(neighbour);
                mx_time[neighbour] = max(mx_time[neighbour] , mx_time[node] + time[node]);
            }
        }
        int res = 0;
        for (int i=0;i<n;i++){
            res = max(res , mx_time[i] + time[i]);
        }
        return res;
    }
};