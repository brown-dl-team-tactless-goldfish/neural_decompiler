class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int r = 0;
        int c = grid.at(0).size() - 1;
        int n = grid.size();
        int count = 0;
        while(r < grid.size() && c >= 0) { 
            if(grid[r][c] < 0) {
                count += n - r;
                c--;
            }
            else {
                r++;
            }
        }
        return count;
    }
};