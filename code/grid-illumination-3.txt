class Solution {
    vector<pair<int, int>> deltas = {{0,0}, {-1,-1}, {-1,0}, {-1, 1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1}};
public:
    vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        unordered_map<int, int> rows, cols, diag1, diag2;
        int l = lamps.size();
        int q = queries.size();
        set<pair<int, int>> grid;
        for(int i = 0; i<l; i++) {
            int r = lamps[i][0], c = lamps[i][1];
            if(grid.find({r,c}) != grid.end()) continue;
            grid.insert({r,c});
            //illuminating row
            if(rows.find(r) == rows.end()) rows[r] = 1;
            else rows[r]++;
            //illuminating col
            if(cols.find(c) == cols.end()) cols[c] = 1;
            else cols[c]++;
            //illuminating left diagonal
            if(diag1.find(r-c) == diag1.end()) diag1[r-c] = 1;
            else diag1[r-c]++;
            //illuminating right diagonal
            if(diag2.find(r+c) == diag2.end()) diag2[r+c] = 1;
            else diag2[r+c]++;
        }
        //queries
        vector<int> ans(q);
        for(int i = 0; i<q; i++) {
            int r = queries[i][0], c = queries[i][1];
            bool res = false;
            if(rows.find(r) != rows.end() && rows[r] > 0) {
                res = true;
            }
            else if(cols.find(c) != cols.end() && cols[c] > 0) {
                res = true;
            }
            else if(diag1.find(r-c) != diag1.end() && diag1[r-c] > 0) {
                res = true;
            }
            else if(diag2.find(r+c) != diag2.end() && diag2[r+c] > 0) {
                res = true;
            }
            ans[i] = ((res)? 1: 0);
            for(int i = 0; i<9; i++) {
                int x = r + deltas[i].first, y = c + deltas[i].second;
                if(x<0 || x==n || y<0 || y==n) continue;
                if(grid.find({x,y}) != grid.end()) {
                    grid.erase({x,y});
                    rows[x]--;
                    cols[y]--;
                    diag1[x-y]--;
                    diag2[x+y]--;
                }
            }
        }
        return ans;
    }
};