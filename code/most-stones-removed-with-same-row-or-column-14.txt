class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        
        int res = 0;
        int n = stones.size();
        vector<bool> visited(n, false);
        
        for(int i=0; i<n; i++)
        {
            if(!visited[i])
                res += dfs(stones, visited, i) - 1;
        }
        
        return res;
    }
    
    int dfs(vector<vector<int>>& stones, vector<bool>& visited, int curr)
    {
        if(visited[curr]) return 0;
        int ret = 1;
        visited[curr] = true;
        
        for(int i=0; i<stones.size(); i++)
        {
            if(!visited[i] && (stones[i][0] == stones[curr][0] || stones[curr][1] == stones[i][1]))
                ret += dfs(stones, visited, i);
        }
        return ret;
    }
};