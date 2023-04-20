#define maxn 20
int fx[] = {-1, 1, 0, 0};
int fy[] = {0, 0, -1, 1};

class Solution {
public:
    int n, m, ans, vis[maxn][maxn], maze_ans[maxn][maxn];

    bool valid(int x, int y, vector<vector<int>>& grid) {
        if(x >= 0 and x < n and y >= 0 and y < m and grid[x][y] and !vis[x][y]) return true;
        else return false;
    }

    void solve(int r, int c, int jewel, vector<vector<int>>& grid)
    {
        ans = max(ans, jewel);

        for(int k=0; k<4; k++) {
            int x = r + fx[k];
            int y = c + fy[k];
            if(valid(x, y, grid)) {
                vis[x][y] = 1;
                solve(x, y, jewel + grid[x][y], grid);
                vis[x][y] = 0;
            }
        }
    }

    int getMaximumGold(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                solve(i, j, 0, grid);
            }
        }
        return ans;
    }
};