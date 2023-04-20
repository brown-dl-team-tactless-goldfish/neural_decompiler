class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size()<n-1){
            return -1;
        }
        vector<vector<int>> adjList(n);
        for(auto& conn: connections){
            adjList[conn[0]].push_back(conn[1]);
            adjList[conn[1]].push_back(conn[0]);
        }
        vector<bool> visited(n, false);
        int ans = 0;
        for(int i=0; i<n; i++){
            if (!visited[i]){
                visited[i] = true;
                ans++;
                queue<int> q;
                q.push(i);
                while(!q.empty()){
                    int c = q.front();
                    q.pop();
                    for(int nxt: adjList[c]){
                        if (!visited[nxt]){
                            visited[nxt] = true;
                            q.push(nxt);
                        }
                    }
                }
            }
        }
        return ans-1;
    }
};