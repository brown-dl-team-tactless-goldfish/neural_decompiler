class Solution {
    int rowCount(vector<vector<int>> &board) {
        map<vector<int>, vector<int>> mp;
        for (int i = 0; i < board.size(); ++i) {
            mp[board[i]].push_back(i);
        }
        // after the moving, all even numbered rows are the same
        // so ar the odd numbered rows
        if (mp.size() != 2) return -1;
        
        // their numbers shoud not differ by more than one
        auto it = mp.begin();
        int count1 = it->second.size();
        ++it;
        int count2 = it->second.size();
        if (abs(count1 - count2) > 1) return -1;
        
        // look at the row with potential more appearances 
        it = mp.begin();
        if (count2 > count1) ++it;
        int even = 0, odd = 0;
        for (int &i : it->second) {
            if (i % 2 == 0) ++even;
            else ++odd;
        }
        if (board.size() % 2 == 0) return min(even, odd); 
        else return odd;
    }
public:
    int movesToChessboard(vector<vector<int>> &board) {
        int n = board.size(), ret1 = rowCount(board);
        if (ret1 == -1) return -1;
        
        vector<vector<int>> a(n, vector<int>(n));
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board.size(); ++j) {
                a[j][i] =  board[i][j];
            }
        }
        int ret2 = rowCount(a);
        if (ret2 == -1) return -1;
        return ret1 + ret2;
    }
};