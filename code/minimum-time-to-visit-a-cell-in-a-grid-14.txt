class Solution {
public:

    vector<pair<int,int>> dir{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int n,m;
    int minimumTime(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();

        if(grid[0][1]>1 and grid[1][0]>1) return -1;


        vector<vector<bool>>vis(n,vector<bool>(m,false));
        priority_queue<vector<int>,vector<vector<int>>,greater<vector<int>>>pq;
        // t i j
        pq.push({0,0,0});

        while(!pq.empty()){
            auto temp = pq.top();
            pq.pop();
            int t = temp[0];
            int x = temp[1];
            int y = temp[2];

            if(x == n-1 and y == m-1) return t;

            if(vis[x][y]) continue;

            vis[x][y] = true;

            for(auto it : dir){
                int xx = it.first + x;
                int yy = it.second + y;
                if(xx<0 || yy<0 || xx>=n || yy>=m || vis[xx][yy]) continue;
                bool wait = ((grid[xx][yy] - t)%2 == 0);
                pq.push({max(t+1,wait+grid[xx][yy]),xx,yy});
            }
        }
        return -1;
        
    }
};