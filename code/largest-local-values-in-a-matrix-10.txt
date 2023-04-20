class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {

        int n=grid.size();
        int m=grid[0].size();
        vector<vector<int>> ans;

    int p = n - 2;
    int q = m - 2;
    for (int i = 0; i < p; i++)
    {
    vector<int> v;
    for (int j = 0; j < q; j++)
    {
    int maxx = 0;
    int maxx1 = max(grid[i][j + 1], max(grid[i][j], grid[i][j + 1 + 1]));
    int maxx2 = max(grid[i + 1][j + 1], max(grid[i + 1][j], grid[i + 1][j + 1 + 1]));
    int maxx3 = max(grid[i + 1 + 1][j + 1], max(grid[i + 1 + 1][j], grid[i + 1 + 1][j + 1 + 1]));
    maxx = max(maxx1, max(maxx2, maxx3));
    v.push_back(maxx);
    }
    ans.push_back(v);
    }
    return ans;

    }
};