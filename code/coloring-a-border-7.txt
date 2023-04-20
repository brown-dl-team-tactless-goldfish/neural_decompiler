class Solution {
public:
    
    vector<vector<bool>> visited;
    vector<vector<int>> copy;
    int r, c, original;
    
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0, int color) {
        r = grid.size();
        c = grid[0].size();
        original = grid[r0][c0];
        copy = grid;
        visited = vector<vector<bool>>(r, vector<bool>(c, false));
        visit(grid, color, r0, c0);
        return copy;
    }
    
    void visit(vector<vector<int>>& grid, int color, int x, int y){
        visited[x][y] = true;
        if (x==0 || grid[x-1][y]!=original){
            copy[x][y] = color;
        }else if (!visited[x-1][y]){
            visit(grid, color, x-1, y);
        }
        if (x==r-1 || grid[x+1][y]!=original){
            copy[x][y] = color;
        }else if (!visited[x+1][y]){
            visit(grid, color, x+1, y);
        }
        if (y==0 || grid[x][y-1]!=original){
            copy[x][y] = color;
        }else if (!visited[x][y-1]){
            visit(grid, color, x, y-1);
        }
        if (y==c-1 || grid[x][y+1]!=original){
            copy[x][y] = color;
        }else if (!visited[x][y+1]){
            visit(grid, color, x, y+1);
        }
    }
};