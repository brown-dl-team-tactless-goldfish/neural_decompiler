class Solution {
public:
    bool check(bool hor, int x, int y, const vector<vector<char>>& board, const string &word) {
        int i, j, W = word.size();
        if (hor) {
            for (j = y; j < y + W; j++)
                if (board[x][j] != ' ' && board[x][j] != word[j - y])
                    return false;
        }
        else {
            for (i = x; i < x + W; i++)
                if (board[i][y] != ' ' && board[i][y] != word[i - x])
                    return false;
        }
        return true;
    }
    bool placeWordInCrossword(vector<vector<char>>& board, string word) {
        string rev = word;
        reverse(rev.begin(), rev.end());
        
        int i, j, W = word.size(), m = board.size(), n = board[0].size();
        vector<vector<int>> ver(m, vector<int>(n, 0)), hor(m, vector<int>(n, 0));
        
        for (i = m - 1; i >= 0; i--) {
            for (j = n - 1; j >= 0; j--) {
                if (board[i][j] == '#')
                    continue;
                hor[i][j] = ver[i][j] = 1;
                if (j + 1 < n) {
                    hor[i][j] += hor[i][j + 1];
                    hor[i][j + 1] = 0;
                }
                if (i + 1 < m) {
                    ver[i][j] += ver[i + 1][j];
                    ver[i + 1][j] = 0;
                }
            }
        }
        
        for (i = 0; i < m; i++) {
            for (j = 0; j < n; j++) {
                if (hor[i][j] == W) {
                    if (check(true, i, j, board, word) || check(true, i, j, board, rev))
                        return true;
                }
                if (ver[i][j] == W) {                    
                    if (check(false, i, j, board, word) || check(false, i, j, board, rev))
                        return true;                    
                }
            }
        }
        return false;
    }
};