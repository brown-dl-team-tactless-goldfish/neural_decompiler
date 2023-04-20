class Solution {
private:
    vector<vector<int>> indices = {{1,1}, {1,0} ,{1,-1}};
    int rsize=0;
    int colsize=0;
    int dp[100][100][100];
public:
    int recur(vector<vector<int>>& grid, int row, int col1, int col2)
    {
            
        if(row<0 or col1<0  or col2<0 or row>=rsize or col1>=colsize  or col2>=colsize)
           return 0;
        
        int sum=0;
        
        if(dp[row][col1][col2]!=-1)
            return dp[row][col1][col2];
        
        for(int i=0;i<indices.size();i++)
        {
                int a=row,b=col1;
                a += indices[i][0];
                b += indices[i][1];
            
            for(int j=0;j<indices.size();j++)
            {
                int c=row,d=col2;
                c += indices[j][0];
                d += indices[j][1];
                
                if(a<0 or b<0 or c<0 or d<0 or a>=rsize or b>=colsize or c>=rsize or d>=colsize)
                  continue;
                
                if(a==c and b==d) 
                  continue;
                

                sum= max(sum, grid[a][b]+grid[c][d] + recur(grid, a, b, d));
                
            }
        }
        
        return dp[row][col1][col2]=sum;
    }
    int cherryPickup(vector<vector<int>>& grid) 
    {
        rsize=grid.size();
        colsize=grid[0].size();
        
        memset(dp,-1,sizeof(dp));
        
        return recur( grid,0,0,grid[0].size()-1) +grid[0][0]+grid[0][grid[0].size()-1];
    
    }
};