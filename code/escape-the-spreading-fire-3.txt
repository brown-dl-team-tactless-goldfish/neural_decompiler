class Solution {
    static constexpr int dir[5] = {-1, 0, 1, 0, -1};
public:
    int maximumMinutes(vector<vector<int>>& grid) {
        int R = grid.size(),
            C = grid[0].size();
        
        vector<vector<int>> fire(R, vector<int>(C, INT_MAX));
        queue<array<int, 3>> q;
        for(int r=0; r<R; ++r){
            for(int c=0; c<C; ++c){
                if(grid[r][c] == 1){
                    fire[r][c] = 0;
                    q.push({r, c, 0});
                }
                else if(grid[r][c] == 2)
                    fire[r][c] = -1;
            }
        }
        while(!q.empty()){
            auto [r, c, t] = q.front();
            q.pop();
            for(int i=0; i<4; ++i){
                int nr = r + dir[i],
                    nc = c + dir[i+1];
                if(nr>=0 && nr<R && nc>=0 && nc<C && fire[nr][nc]>t+1){
                    fire[nr][nc] = t+1;
                    q.push({nr, nc, t+1});
                }
            }
        }
        int l = 0,
            r = R*C + 1;
        vector<vector<int>> visited(R, vector<int>(C));
        while(l <= r){
            int mid = l + ((r-l)>>1);
            for(auto& row:visited)
                fill(row.begin(), row.end(), INT_MAX);
            if(possible(0, 0, mid, visited, fire))
                l = mid+1;
            else
                r = mid-1;
        }
        
        return r == R*C + 1 ? 1e9 : r;
    }
private:
    bool possible(int r, int c, int t, vector<vector<int>>& visited, vector<vector<int>>& fire) {
        if(r == fire.size()-1 && c == fire[0].size()-1)
            return true;
        if(fire[r][c] == t)
            return false;
        visited[r][c] = t;
        for(int i=0; i<4; ++i){
            int nr = r + dir[i],
                nc = c + dir[i+1];
            if(nr>=0 && nr<fire.size() && nc>=0 && nc<fire[0].size() && visited[nr][nc]>t+1 && fire[nr][nc]>=t+1 && possible(nr, nc, t+1, visited, fire))
                return true;
        }
        
        return false;
    }
};