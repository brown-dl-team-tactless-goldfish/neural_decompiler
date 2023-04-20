class Solution {
public:
    bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
        char opp = color == 'B' ? 'W' : 'B';
        
        int a[8] = {0,0,1,-1,1,-1,-1,1};
        int b[8] = {1,-1,0,0,1,-1,1,-1};
        
        for(int k = 0; k < 8; ++k) {
            int x = rMove + a[k], y = cMove + b[k];
            bool seenOpp = false, flag = false;
            for(; x >= 0 && y >= 0 && x < 8 && y < 8; x += a[k], y += b[k]) {
                if(board[x][y] == '.') break;
                else if(board[x][y] != opp) {
                    flag = true;
                    break;
                }
                else if(!seenOpp) seenOpp = true;
            }
            if(seenOpp && flag) return true;
        }
        return false;
    }
};