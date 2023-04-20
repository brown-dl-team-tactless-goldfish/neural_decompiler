class Solution {
public:
    int memo[5][6][5][6][301];
    int n;
    int minimumDistance(string s) {
        n = s.size();
        memset(memo, -1, sizeof(memo));
        int res = 1e9;
        for(int i = 0; i < 26; i++)
            for(int j = 0; j < 26; j++)
                res = min(res, dp(s, 0, i / 6, i % 6, j / 6, j % 6));
        return res;
    }
    int dp(string& s, int idx, int r1, int c1, int r2, int c2){
        if(idx == n)
            return 0;
        if(memo[r1][c1][r2][c2][idx] != -1)
            return memo[r1][c1][r2][c2][idx];
        int a = s[idx] - 'A', r = a / 6, c = a % 6;
        return memo[r1][c1][r2][c2][idx] = min(abs(r - r1) + abs(c - c1) + dp(s, idx + 1, r, c, r2, c2), abs(r - r2) + abs(c - c2) + dp(s, idx + 1, r1, c1, r, c));
    }
};