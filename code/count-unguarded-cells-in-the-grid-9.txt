class Solution {
public:
    int countUnguarded(int n, int m, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<char>> grid(n,vector<char>(m,'0'));
        for(int i=0;i<guards.size();i++)
        {
            int r = guards[i][0];
            int c = guards[i][1];
            grid[r][c] = 'G';
        }
        for(int i=0;i<walls.size();i++)
        {
            int r = walls[i][0];
            int c = walls[i][1];
            grid[r][c] = 'W';
        }
        for(int i=0;i<guards.size();i++)
        {
            int r = guards[i][0];
            int c = guards[i][1];
            for(int j=c-1;j>=0;j--)
            {
                if(grid[r][j]=='W' || grid[r][j]=='G')
                break;
                if(grid[r][j]=='0')
                grid[r][j] = '1';
            }
            for(int j=c+1;j<m;j++)
            {
                if(grid[r][j]=='W' || grid[r][j]=='G')
                break;
                if(grid[r][j]=='0')
                grid[r][j] = '1';
            }
            for(int j=r-1;j>=0;j--)
            {
                if(grid[j][c]=='W' || grid[j][c]=='G')
                break;
                if(grid[j][c]=='0')
                grid[j][c] = '1';
            }
            for(int j=r+1;j<n;j++)
            {
                if(grid[j][c]=='W' || grid[j][c]=='G')
                break;
                if(grid[j][c]=='0')
                grid[j][c] = '1';
            }
        }
        int cnt=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j]=='0')
                cnt++;
            }
        }
        return cnt;
    }
};