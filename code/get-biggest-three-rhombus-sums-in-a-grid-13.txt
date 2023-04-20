class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        vector<vector<int> > ld = grid, rd = grid;//ld = left diagonal, rd = right diagonal
        int m = grid.size();
        int n = grid[0].size();
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                int pi = i - 1;
                int prevj = j - 1;
                if(pi >= 0 && prevj >= 0) ld[i][j] += ld[pi][prevj];
                prevj = j + 1;
                if(pi >= 0 && prevj < n) rd[i][j] += rd[pi][prevj];
            }
        }
        map<int, int> cnt;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                ++cnt[grid[i][j]];
                for(int k = 1; k <=max(m, n); ++k) {
                    int left = j - k;
                    int right = j + k;
                    int bot = i + 2 * k;
                    if(left < 0 || right >= n || bot >= m) continue;
                    int sum = rd[i + k][left] - rd[i][j] 
                                         + ld[i + k][right] - ld[i][j] 
                                         + ld[bot][j] - ld[i + k][left]
                                         + rd[bot][j] - rd[i + k][right]
                                         + grid[i][j] - grid[bot][j];
                    ++cnt[sum];
                }
                while(cnt.size() > 3) {
                    auto it = cnt.begin();
                    cnt.erase(it);
                }
            }
        }
        vector<int> ans;
        for(auto it = cnt.rbegin(); it != cnt.rend(); it++) {
            ans.push_back(it->first);
            if(ans.size() >= 3) return ans;
        }
        return ans;
    }
};