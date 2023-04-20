class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& g, int k) {
        int top = 0, l = 0, btm = g.size()-1, r = g[0].size()-1;
        while(top < btm && l < r) {
            int total = 2*(btm-top)+2*(r-l), shift = k%total;
            while(shift-- > 0) {
                int last = g[top][l];
                for(int c = l; c < r; c++) g[top][c] = g[top][c+1];
                for(int rr = top; rr < btm; rr++) g[rr][r] = g[rr+1][r];
                for(int c = r; c > l; c--) g[btm][c] = g[btm][c-1];
                for(int rr = btm; rr > top+1; rr--) g[rr][l] = g[rr-1][l];
                g[top+1][l] = last;
            }
            top++;
            btm--;
            l++;
            r--;
        }
        return g;
    }
};