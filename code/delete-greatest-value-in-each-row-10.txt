class Solution {
public:
    int deleteGreatestValue(vector<vector<int>>& grid) {

    int m=grid.size();
    int n=grid[0].size();

    for(int i=0;i<m;i++)
        sort(grid[i].begin(),grid[i].end());

    int sum=0;
    for(int i=0;i<n;i++)
    {
        int value=0;
        for(int j=0;j<m;j++)
            value=max(value,grid[j][i]);
        sum+=value;
    }
    return sum;

    }
};