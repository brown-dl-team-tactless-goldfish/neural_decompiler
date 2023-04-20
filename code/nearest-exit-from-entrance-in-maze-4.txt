struct MazeRecord
{
    char cRow;
    char cCol;
    short sDistance;

    struct MazeRecord* pstNext;
};

struct MazeRecord* AddMazeRecord(struct MazeRecord* pstTail, char cRow, char cCol, short sDistance)
{
    if(pstTail->pstNext)
    {
        pstTail = pstTail->pstNext;
    }
    else
    {
        pstTail->pstNext = (struct MazeRecord*) malloc(sizeof(struct MazeRecord));
        pstTail = pstTail->pstNext;
        pstTail->pstNext = NULL;;
    }

    pstTail->cRow = cRow;
    pstTail->cCol = cCol;
    pstTail->sDistance = sDistance;

    return pstTail;
}

int nearestExit(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize){
    char cMazeSize = mazeSize - 1, cMazeColSize = *mazeColSize - 1;

    struct MazeRecord* pstHead = (struct MazeRecord*) malloc(sizeof(struct MazeRecord));
    pstHead->cRow = *entrance;
    pstHead->cCol = *(entrance + 1);
    pstHead->sDistance = 0;
    pstHead->pstNext = NULL;
    maze[pstHead->cRow][pstHead->cCol] = ',';

    short sRet = 0;
    struct MazeRecord* pstTail = pstHead;
    while(pstHead)
    {
        // check up
        if(pstHead->cRow && maze[pstHead->cRow-1][pstHead->cCol] == '.')
        {
            if(pstHead->cRow-1 == 0 || pstHead->cCol == 0 || pstHead->cCol == cMazeColSize)
            {
                sRet = pstHead->sDistance + 1;
                break;
            }
            else
            {
                maze[pstHead->cRow-1][pstHead->cCol] = ',';
                pstTail = AddMazeRecord(pstTail, pstHead->cRow-1, pstHead->cCol, pstHead->sDistance+1);
            }
        }

        // check left
        if(pstHead->cCol && maze[pstHead->cRow][pstHead->cCol-1] == '.')
        {
            if(pstHead->cCol-1 == 0 || pstHead->cRow == 0 || pstHead->cRow == cMazeSize)
            {
                sRet = pstHead->sDistance + 1;
                break;
            }
            else
            {
                maze[pstHead->cRow][pstHead->cCol-1] = ',';
                pstTail = AddMazeRecord(pstTail, pstHead->cRow, pstHead->cCol-1, pstHead->sDistance+1);
            }
        }

        // check right
        if(pstHead->cCol < cMazeColSize && maze[pstHead->cRow][pstHead->cCol+1] == '.')
        {
            if(pstHead->cCol+1 == cMazeColSize || pstHead->cRow == 0 || pstHead->cRow == cMazeSize)
            {
                sRet = pstHead->sDistance + 1;
                break;
            }
            else
            {
                maze[pstHead->cRow][pstHead->cCol+1] = ',';
                pstTail = AddMazeRecord(pstTail, pstHead->cRow, pstHead->cCol+1, pstHead->sDistance+1);
            }
        }

        // check down
        if(pstHead->cRow < cMazeSize && maze[pstHead->cRow+1][pstHead->cCol] == '.')
        {
            if(pstHead->cRow+1 == cMazeSize || pstHead->cCol == 0 || pstHead->cCol == cMazeColSize)
            {
                sRet = pstHead->sDistance + 1;
                break;
            }
            else
            {
                maze[pstHead->cRow+1][pstHead->cCol] = ',';
                pstTail = AddMazeRecord(pstTail, pstHead->cRow+1, pstHead->cCol, pstHead->sDistance+1);
            }
        }

        if(pstHead == pstTail) break;

        struct MazeRecord* pstTmp = pstHead;
        pstHead = pstHead->pstNext;
        pstTmp->pstNext = pstTail->pstNext;
        pstTail->pstNext = pstTmp;
    }

    while(pstHead)
    {
        pstTail = pstHead;
        pstHead = pstHead->pstNext;
        free(pstTail);
    }

    return sRet? sRet: -1;
}