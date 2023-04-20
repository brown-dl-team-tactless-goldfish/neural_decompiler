
int rules(int **copyBoard, int row , int col, int m, int n)
{
    int live = 0;
    int dead = 0;
    int rowi = row-1;
    int colj = col-1;
    for(;rowi<=row+1 && rowi<m;rowi++)
    {
        if(rowi< 0)
        {
            continue;
        }
        colj = col-1;
        for(;colj<=col+1 && colj<n;colj++)
        {
            if(colj<0)
                continue;
             if(rowi == row && colj == col )
                continue;
            if((copyBoard)[rowi][colj] == 1)
                live++;
           
        }
    }
    return live;
}

void printBoard(int **board, int row , int col)
{
    for(int i = 0;i<row;i++)
    {
        for(int j = 0;j<col;j++ )
        {
            printf(" %d ",board[i][j]);
        }
        printf("\n");
    }
    
    printf("\n\n\n\n\n");
}

void gameOfLife(int** board, int boardSize, int* boardColSize){
    int** copyBoard= calloc(1,sizeof(int*) * boardSize);
     //printBoard(board, boardSize, boardColSize[0]);
    //int copyBoard[boardSize][* boardColSize];
    for(int row = 0;row<boardSize;row++)
    {
        copyBoard[row] = malloc(sizeof(int) * (boardColSize[0]));
        for(int col = 0;col<boardColSize[0];col++ )
        {
           
            copyBoard[row][col] = board[row][col];
        }
    }
    
        
   
    //printBoard(copyBoard, boardSize, boardColSize[0]);
    
    for(int row = 0;row<boardSize;row++)
    {
        for(int col = 0;col<boardColSize[row];col++ )
        {
            int live = rules(copyBoard,row, col, boardSize, (*boardColSize));
            if(live>3 && board[row][col]==1 ) //over-population
                board[row][col] = 0;
            else if(live==3 && board[row][col]==0) //repro
                board[row][col] = 1;
            else if(live<2 && board[row][col]==1) //under-population
                board[row][col] = 0;
            live = 0;
        }
    }
}