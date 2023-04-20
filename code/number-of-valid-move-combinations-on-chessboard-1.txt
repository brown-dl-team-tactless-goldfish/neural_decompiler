class Solution {
public:
    void dfs(int cur, bool vis[8][8][8]) {
        if (cur == n) {
            ++res;
            return;
        }
        int x = poss[cur][0] - 1, y = poss[cur][1] - 1;
        
        // move.
        vector<pair<int, int>> dirs;
        if (ps[cur] == "rook") {
            dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        } else if (ps[cur] == "queen") {
            dirs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        } else {
            dirs = {{-1, -1}, {1, 1}, {-1, 1}, {1, -1}};
        }
        for (int i = 0; i < dirs.size(); ++i) {
            int dx = dirs[i].first, dy = dirs[i].second;
            for (int j = 1; ; ++j) {
                int xx = x + dx * j;
                int yy = y + dy * j;
                if (xx < 0 || xx >= 8 || yy < 0 || yy >= 8 || vis[j][xx][yy]) {
                    while (--j >= 1) {
                        int xx = x + dx * j;
                        int yy = y + dy * j;
                        vis[j][xx][yy] = false;
                    }
                    break;
                }
                vis[j][xx][yy] = true;
                bool ok = true;
                for (int k = j + 1; k < 8; ++k) {
                    if (vis[k][xx][yy]) {
                        ok = false;
                        break;
                    }
                }
                if (!ok)
                    continue;
                for (int k = j; k < 8; ++k) {
                    vis[k][xx][yy] = true;
                }
                dfs(cur + 1, vis);
                for (int k = j + 1; k < 8; ++k) {
                    vis[k][xx][yy] = false;
                }
            }
        }
        
        // stay.
        bool ok = true;
        for (int i = 1; i < 8; ++i)
            if (vis[i][x][y]) {
                ok = false;
                break;
            }
        if (!ok)
            return;
        for (int i = 1; i < 8; ++i)
            vis[i][x][y] = true;
        dfs(cur + 1, vis);
        for (int i = 1; i < 8; ++i)
            vis[i][x][y] = false;
    }
    
    int countCombinations(vector<string>& pieces, vector<vector<int>>& positions) {
        res = 0;
        ps = pieces;
        poss = positions;
        n = ps.size();
        bool vis[8][8][8] = {0};
        dfs(0, vis);
        return res;
    }
    
    int n;
    int res;
    vector<string> ps;
    vector<vector<int>> poss;
};