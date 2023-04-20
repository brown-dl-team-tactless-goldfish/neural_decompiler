class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
      // grid size
      const int R = grid.size();
      const int C = grid[0].size();

      // record the reach of 1's from every cell
      auto right = grid;
      auto down  = move(grid);
      for (int r = 0; r < R; ++r)
        for (int c = C-2; c >= 0; --c)
          right[r][c] *= right[r][c+1] + 1;
      for (int c = 0; c < C; ++c)
        for (int r = R-2; r >= 0; --r)
          down[r][c] *= down[r+1][c] + 1;

      // find the largest 1-bordered square
      int length = 0;
      for (int r = 0; r < R - length; ++r)
        for (int c = 0; c < C - length; ++c)
          for (int dist = min(right[r][c], down[r][c]); dist > length; --dist)
            if (dist <= min(right[r+dist-1][c], down[r][c+dist-1]))
              length = dist;

      return length * length;        
    }
};