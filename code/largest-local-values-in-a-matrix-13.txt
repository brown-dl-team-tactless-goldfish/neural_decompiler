class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        
        int n = grid.size();
        
        vector<vector<int>> ans(n-2,vector<int>(n-2));
        
        
        for(int i=0;i<n-2;i++){
            for(int j=0;j<n-2;j++)
                ans[i][j] = maxIn3x3(grid, i, j);
        }    
        
        return ans;
    }
    
    
    int maxIn3x3(vector<vector<int>> &arr, int i, int j)
	{
        int maxVal = INT_MIN;
        
        for(int x = i ; x < i+3 ; x++){
            for(int y = j; y < j+3 ; y++)
                maxVal = max(arr[x][y], maxVal);
        }

        return maxVal;
    }
    
};
