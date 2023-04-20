class Solution {
public:
    int ways(vector<string>& p, int k) {
        rs = p.size();
        cs = p[0].size();
        dp.assign(rs, vector<vector<int>>(cs, vector<int>(k+1, -1)));
        cnt.assign(rs+1, vector<int>(cs+1, 0)); // cnt[i][j] is number of A in row i from col 0 to j-1
        cnt2.assign(cs+1, vector<int>(rs+1, 0)); //cnt2[j][i] is the number of A in column j from row 0 to row i-1 
        for (int i = 0; i < rs; i++) {
            for (int j = 0; j < cs; j++) {
                cnt[i][j+1] = (p[i][j] == 'A') + cnt[i][j];
            }
        }
        for (int j = 0; j < cs; j++) {
            for (int i = 0; i < rs; i++) {
                cnt2[j][i+1] = (p[i][j] == 'A') + cnt2[j][i];
            }
        }      
        return f(0, 0, k);
    }
    
    int f(int i, int j, int k) {
        if (dp[i][j][k] != -1) return dp[i][j][k];
        int sum = cnt[i][cs]-cnt[i][j];
        for (int r = i+1; r < rs; r++) {
            sum += cnt[r][cs]-cnt[r][j];
        }
        if (sum < k) return dp[i][j][k] = 0; 
        if (k==1) return dp[i][j][k] = 1;
        
        long res = 0;
        int upper = cnt[i][cs]-cnt[i][j];
        for (int r = i+1; r < rs; r++) {
            if (upper > 0) {
                res = (f(r, j, k-1)%MOD + res)%MOD;
            }
            upper += cnt[r][cs]-cnt[r][j];
        }
        
        int left = cnt2[j][rs]-cnt2[j][i];
        for (int c = j+1; c < cs; c++) {
            if (left > 0) {
                res = (f(i, c, k-1)%MOD + res)%MOD;
            }
            left += cnt2[c][rs]-cnt2[c][i];
        }
        return dp[i][j][k] = res;
    }
    
    int MOD = 1e9+7;
    int rs, cs;
    vector<vector<vector<int>>> dp; // dp[i][j][k] stores answer for f(i, rows-1, j, cols-1, k)
    vector<vector<int>> cnt, cnt2;
};