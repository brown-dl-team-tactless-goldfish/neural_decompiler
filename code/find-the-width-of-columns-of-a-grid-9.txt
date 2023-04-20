class Solution {
public:
    vector<int> findColumnWidth(vector<vector<int>>& grid) {
        int m=grid.size(),n=grid[0].size();
        vector<int>ans(n);
        for(int j=0;j<n;++j){
            int len=1;
            for(int i=0;i<m;++i){
                if(grid[i][j]<0) len=max(len,int(log10(-grid[i][j]) + 1)+1);
                else if(grid[i][j]>9) len=max(len,int(log10(grid[i][j]) + 1));
            }
            ans[j]=len;
        }
        return ans;
    }
};