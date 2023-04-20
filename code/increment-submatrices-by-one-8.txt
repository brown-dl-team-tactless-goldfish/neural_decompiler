class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> ans(n,vector<int>(n+1));
        for(auto&i:queries)
            for(int r=i[0];r<=i[2];++r)++ans[r][i[1]],--ans[r][i[3]+1];
        for(int i=0;i<n;++i){
            for(int j=1;j<n;++j) ans[i][j]+=ans[i][j-1];
            ans[i].pop_back();
        }
        return ans;
    }
};