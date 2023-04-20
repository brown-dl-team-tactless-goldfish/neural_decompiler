class Solution {
public:
    bool isPossibleToCutPath(vector<vector<int>>& grid) {
        int n=grid.size();
        int m=grid[0].size();
        vector<int>v(m+n-1,0);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j])
                    v[i+j]++;
            }
        }
        for(int i=1;i<v.size()-1;i++)
        {
            
            if(v[i]<=1) return true; 
        }
        return false;
    }
};