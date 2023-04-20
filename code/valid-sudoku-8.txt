bool isValidSudoku(char** board, int boardRowSize, int boardColSize) {
    char tmpR[9][9] = {0};
    char tmpC[9][9] = {0};
    char tmpI[9][9] = {0};
    int num;
    int index;
    for(int i = 0 ; i < 9;++i){
        for(int j = 0; j < 9; ++j){
            if(board[i][j] == '.'){
                continue;
            }
            num = board[i][j] - '1';
            index = (i/3)*3 + j/3;
            if(tmpR[i][num]|tmpC[j][num]|tmpI[index][num]){
                return false;
            }
            tmpR[i][num] = tmpC[j][num] = tmpI[index][num] = 1;
        }
    }
    return true;
}