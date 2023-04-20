class Solution {
public:
    map<int, int> hash;
    vector<int> DIR = {1, 0, -1, 0, 1};
    int n, m;
    int cutOffTree(vector<vector<int>>& f) {
        n = f.size(), m = f[0].size();
        int cur = 0, result = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(f[i][j] > 1)
                    hash[f[i][j]] = i * m + j;
        
        for(auto& a: hash){
            int steps = helper(f, cur, a.second);
            if(steps == -1e9) return -1;
            result += steps;
            cur = a.second;
        }
        return result;
    }
    
    int helper(vector<vector<int>>& f, int cur, int target){
        queue<int> q;
        int steps = 0;
        q.push({cur});
        vector<vector<bool>> vis(n, vector<bool>(m));
        while(!q.empty()){
            int sz = q.size();
            while(sz--){
                int pos = q.front(), r = pos / m, c = pos % m;
                q.pop();
                if(pos == target)
                    return steps;
                for(int k = 0; k < 4; k++){
                    int nr = r + DIR[k], nc = c + DIR[k + 1];
                    if(nr < 0 || nr == n || nc < 0 || nc == m || vis[nr][nc] || !f[nr][nc])
                        continue;
                    q.push({nr * m + nc});
                    vis[nr][nc] = true;
                }
            }
            steps++;
        }
        return -1e9;
    }
};