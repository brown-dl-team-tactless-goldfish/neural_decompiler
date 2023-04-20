typedef struct {
    int** rect;
    int rowlen;
    int* collen;
} SubrectangleQueries;


SubrectangleQueries* subrectangleQueriesCreate(int** rectangle, int rectangleSize, int* rectangleColSize) {
    SubrectangleQueries* obj=(SubrectangleQueries * ) malloc (sizeof (SubrectangleQueries));

    obj->rowlen=rectangleSize;
    obj->collen=rectangleColSize;
    obj->rect=rectangle;

    return obj;
}

void subrectangleQueriesUpdateSubrectangle(SubrectangleQueries* obj, int row1, int col1, int row2, int col2, int newValue) {
    int cols=col1;
    int rows=row1;

    while(rows<=row2){
        cols=col1;
        while(cols<=col2){
            obj->rect[rows][cols]=newValue;
            cols++;
        }
        rows++;
    }
}

int subrectangleQueriesGetValue(SubrectangleQueries* obj, int row, int col) {
    return obj->rect[row][col];
}

void subrectangleQueriesFree(SubrectangleQueries* obj) {
    free(obj);
}

/**
 * Your SubrectangleQueries struct will be instantiated and called as such:
 * SubrectangleQueries* obj = subrectangleQueriesCreate(rectangle, rectangleSize, rectangleColSize);
 * subrectangleQueriesUpdateSubrectangle(obj, row1, col1, row2, col2, newValue);
 
 * int param_2 = subrectangleQueriesGetValue(obj, row, col);
 
 * subrectangleQueriesFree(obj);
*/