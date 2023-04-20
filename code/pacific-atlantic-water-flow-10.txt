class Solution {
private:
    int Nr, Nc;
    
    void dfs(vector<vector<int>>& matrix, int r, int c, vector<vector<bool>>& visited) {
        visited[r][c] = true;
        if (r > 0    and matrix[r][c] <= matrix[r-1][c] and !visited[r-1][c]) dfs(matrix, r-1, c, visited);
        if (r < Nr-1 and matrix[r][c] <= matrix[r+1][c] and !visited[r+1][c]) dfs(matrix, r+1, c, visited);
        if (c > 0    and matrix[r][c] <= matrix[r][c-1] and !visited[r][c-1]) dfs(matrix, r, c-1, visited);
        if (c < Nc-1 and matrix[r][c] <= matrix[r][c+1] and !visited[r][c+1]) dfs(matrix, r, c+1, visited);
    }
    
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        Nr = matrix.size();
        if (Nr == 0) return vector<vector<int>>();
        Nc = matrix[0].size();
        if (Nc == 0) return vector<vector<int>>();
        // find points that are accessible to Pacific/Atlantic
        vector<vector<bool>> pacific(Nr, vector<bool>(Nc, false));
        vector<vector<bool>> atlantic(Nr, vector<bool>(Nc, false));
        for (int r(0); r < Nr; ++r) {
            dfs(matrix, r, 0, pacific);
            dfs(matrix, r, Nc-1, atlantic);
        }
        for (int c(0); c < Nc; ++c) {
            dfs(matrix, 0, c, pacific);
            dfs(matrix, Nr-1, c, atlantic);
        }
        // generate result vector
        vector<vector<int>> rst;
        for (int r(0); r < Nr; ++r) {
            for (int c(0); c < Nc; ++c) {
                if (pacific[r][c] and atlantic[r][c]) {
                    rst.push_back(vector<int>{ r, c });
                }
            }
        }
        return rst;
    }
};