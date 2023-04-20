class Solution {
public:
    
    // split the area in different part and find individual ones
    
    int surfaceArea(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int bottom_top_area = 2*n*m;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 0) bottom_top_area-=2;
            }
        }
        int eastwest = 0;
        for(int i=0;i<n;i++){
             eastwest+=grid[i][0];
             eastwest+=grid[i][n-1];
            for(int j=0;j<m-1;j++){
                eastwest+=abs(grid[i][j+1]-grid[i][j]);
            }
        }
        int northsouth = 0;
        for(int i=0;i<m;i++){
            northsouth+=grid[0][i];
            northsouth+=grid[m-1][i];
            for(int j=0;j<n-1;j++){
                northsouth+=abs(grid[j+1][i]-grid[j][i]);
            }
        }
        return bottom_top_area+northsouth+eastwest;
    }
};