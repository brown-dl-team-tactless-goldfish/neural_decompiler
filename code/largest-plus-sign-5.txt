class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        vector<vector<bool>> isMine(n, vector<bool>(n, false));
        for (auto& pos: mines) isMine[pos[0]][pos[1]] = true;
        int ans = 0;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                int plusSignSize = dpMaxArm(n, isMine, r, c, 0);
                for (int d = 1; d < 4; ++d)
                    plusSignSize = min(plusSignSize, dpMaxArm(n, isMine, r, c, d));
                ans = max(ans, plusSignSize);
            }
        }
        return ans;
    }

    int DIR[5] = {0, 1, 0, -1, 0};
    int memo[500][500][4] = {};
    int dpMaxArm(int n, vector<vector<bool>>& isMine, int r, int c, int d) {
        if (r < 0 or r >= n or c < 0 or c >= n or isMine[r][c]) return 0;
        if (memo[r][c][d] != 0) return memo[r][c][d];
        return memo[r][c][d] = dpMaxArm(n, isMine, r + DIR[d], c + DIR[d+1], d) + 1;
    }
};