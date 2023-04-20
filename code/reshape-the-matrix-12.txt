int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes){
    
    if(matSize * matColSize[0] != r * c){
        *returnSize = matSize;
        *returnColumnSizes = matColSize;
        return mat;
    }
    
    *returnSize = r;
    *returnColumnSizes = malloc(sizeof(int) * r);
    int **res = malloc(sizeof(int *) * r);
    for(int i = 0; i < r; i++){
        (*returnColumnSizes)[i] = c;
        res[i] = malloc(sizeof(int) * c);
    }
    
    int *flatten = malloc(sizeof(int) * (r * c));
    int index = 0;
    for(int i = 0; i < matSize; i++){
        for(int j = 0; j < matColSize[i]; j++){
            flatten[index++] = mat[i][j];
        }
    }
    
    index = 0;
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            res[i][j] = flatten[index++];
        }
    }
    return res;
}