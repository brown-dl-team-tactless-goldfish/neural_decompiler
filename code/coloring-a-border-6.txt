class Solution {
	void dfs(vector<vector<int>>& grid, int r, int c, int color) {
		if(r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] != color)
			return;

		grid[r][c] = INT_MAX;

		dfs(grid, r + 1, c, color);
		dfs(grid, r - 1, c, color);
		dfs(grid, r, c + 1, color);
		dfs(grid, r, c - 1, color);
	}
public:
	vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0, int color) {
		int rows, cols;

		if((rows = grid.size()) == 0 || (cols = grid[0].size()) == 0)
			return {};

		vector<vector<int>> temp = grid;
		dfs(temp, r0, c0, grid[r0][c0]);

		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++) {
				if(i == 0 || j == 0 || i == rows - 1 || j == cols - 1) {
					if(temp[i][j] == INT_MAX)
						grid[i][j] = color;
				} else {
					if((temp[i][j]) == INT_MAX and 
					   ((temp[i - 1][j] != INT_MAX) || (temp[i + 1][j] != INT_MAX) ||
						(temp[i][j - 1] != INT_MAX) || (temp[i][j + 1] != INT_MAX)))
						grid[i][j] = color;
				}
			}
		}

		return grid;
	}
};