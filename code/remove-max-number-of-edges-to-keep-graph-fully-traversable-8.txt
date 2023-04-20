class Solution {
public:
    int getParent(vector<int>& parent, int i){
        return i == parent[i] ? i : parent[i] = getParent(parent, parent[i]);
    }
    bool doUnion(vector<int>& parent, int i, int j){
        int pi = getParent(parent, i);
        int pj = getParent(parent, j);
        parent[pj] = pi;
        return pi != pj;
    }
    void dfs(vector<vector<int>>& adjList, vector<bool>& vis, int u){
        if(vis[u]){
            return;
        }
        vis[u] = true;
        for(auto v: adjList[u]){
            dfs(adjList, vis, v);
        }
        return;
    }
    bool isConnected(vector<vector<int>>& adjList){
        int n = adjList.size();
        vector<bool> vis(n, false);
        dfs(adjList, vis, 0);
        for(int i = 0; i < n; i++){
            if(!vis[i]){
                return false;
            }
        }
        return true;
    }
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        int A = 1, B = 2, C = (A|B);
        int edgesCount = 0;
        vector<int> alice(n), bob(n);
        vector<vector<int>> adjListAlice(n), adjListBob(n);
        for(int i = 0; i < n; i++){
            alice[i] = bob[i] = i;
        }
        for(auto& edge: edges){
            int type = edge[0], u = edge[1]-1, v = edge[2]-1;
            if(type == C && doUnion(alice, u, v) && doUnion(bob, u, v)){
                adjListAlice[u].push_back(v);
                adjListAlice[v].push_back(u);
                adjListBob[u].push_back(v);
                adjListBob[v].push_back(u);
                edgesCount++;
            }
        }
        for(auto& edge: edges){
            int type = edge[0], u = edge[1]-1, v = edge[2]-1;
            if((type == A) && doUnion(alice, u, v)){
                adjListAlice[u].push_back(v);
                adjListAlice[v].push_back(u);
                edgesCount++;
            }
            if((type == B) && doUnion(bob, u, v)){
                adjListBob[u].push_back(v);
                adjListBob[v].push_back(u);
                edgesCount++;
            }
        }
        return isConnected(adjListAlice) && isConnected(adjListBob) ? edges.size() - edgesCount : -1;
    }
};