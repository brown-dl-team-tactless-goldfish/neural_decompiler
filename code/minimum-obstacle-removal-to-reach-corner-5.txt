#define pi pair<int,int>

class Solution {
public:
    bool isvalid(int i, int j, vector<vector<int>> &grid, int m, int n) {
        return i >= 0 and i < m and j >= 0 and j < n and grid[i][j] != -1;
    }
    
    
    int minimumObstacles(vector<vector<int>>& grid) {
        
        int m(size(grid)), n(size(grid[0]));
        
        int dir[] = {1,0,-1,0,1};
        
        priority_queue<pair<int,pi>, vector<pair<int,pi>>, greater<pair<int,pi>>> pq;
        vector<vector<int>> dist(m, vector<int>(n,INT_MAX));
        dist[0][0] = 0;
        pq.push({0,{0,0}});
        grid[0][0] = -1;
    
        while(!pq.empty()) {
            
            auto cell = pq.top();
            pq.pop();
            int prevdist = cell.first;
            int r = cell.second.first;
            int c = cell.second.second;
            
            if(r + c == m + n - 2) return prevdist;
            
            for(int i = 0; i < 4; i++) {
                int x = r + dir[i];
                int y = c + dir[i+1];
                
                if(isvalid(x,y,grid,m,n) and prevdist + grid[x][y] < dist[x][y]) {
                    
                    dist[x][y] = prevdist + grid[x][y];
                    pq.push({dist[x][y],{x,y}});
                    grid[x][y] = -1;
                }
            }
        }
        
        
        return 0;
        
    }
};