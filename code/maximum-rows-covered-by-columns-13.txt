class Solution 
{
    int m;
    int n;
    vector<bool> selected;
    int ans = 0;
public:
    int maximumRows(vector<vector<int>>& matrix, int numSelect) 
    {
        m = matrix.size();
        n = matrix[0].size();
        
        selected.resize(n);
        dfs(matrix, numSelect, 0);
        
        return ans;
    }
    
    void dfs(vector<vector<int>>& mat, int cnt, int cur)
    {
        if (cnt == 0)
        {
            int rows = 0;
            for (int i = 0; i < m; ++i)
            {
                bool covered = true;
                for (int j = 0; j < n; ++j)
                {
                    if (mat[i][j] == 1 && !selected[j])
                    {
                        covered = false;
                        break;
                    }
                }
                
                if (covered)
                {
                    ++rows;
                }
            }
            
            ans = max(ans, rows);
            return;
        }
        
        for (int k = cur; k < n; ++k)
        {
            selected[k] = true;
            dfs(mat, cnt - 1, k + 1);
            selected[k] = false;
        }
    }
};