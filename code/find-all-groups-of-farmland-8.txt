class Solution {
public:
    vector<vector<int>> ans;
    int n , m;
    vector<int> temp;
    void dfs(vector<vector<int>>&land, int i, int j){
        if(i < 0 || j < 0 || i >= n || j >= m || land[i][j] != 1) return;
        land[i][j] = 2;
        if((i - 1 < 0 && j - 1 < 0) || (i - 1 >= 0 && j - 1 >= 0 && land[i - 1][j] == 0 && land[i][j - 1] == 0) || (i - 1 < 0 && j - 1 >= 0 && land[i][j - 1] == 0) || (j - 1 < 0 && i - 1 >= 0 && land[i - 1][j] == 0)){
            temp.push_back(i);
            temp.push_back(j);
        }
        if((i + 1 >= n && j + 1 >= m) || (i + 1 < n && j + 1 < m && land[i + 1][j] == 0 && land[i][j + 1] == 0) || (i + 1 >= n && j + 1 < m && land[i][j + 1] == 0) || (j + 1 >= m && i + 1 < n && land[i + 1][j] == 0)){
            temp.push_back(i);
            temp.push_back(j);
            ans.push_back(temp);
            temp.clear();
            return;
        }
        // land[i][j] = 2;
        dfs(land, i + 1, j);
        dfs(land, i - 1, j);
        dfs(land, i, j + 1);
        dfs(land, i, j - 1);
    }
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        n = land.size(), m = land[0].size();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++){
                if(land[i][j] == 1) dfs(land, i, j);
            }
        }
        // for(auto c : temp) cout << c << " ";
        return ans;
    }
};