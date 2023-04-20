

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeakGrid(int** mat, int matSize, int* matColSize, int* returnSize){
    *returnSize = 2;

    int i = matSize/2;
    int j = matColSize[i]/2;
    while(1){
        int neighbor_max = mat[i][j];
        int neighbor_i = -1;
        int neighbor_j = -1;
        //Up
        if(i-1 >= 0){
            if(mat[i-1][j] > neighbor_max ){
                neighbor_i = i-1;
                neighbor_j = j;
                neighbor_max = mat[i-1][j];
            }
        }

        //Down
        if(i+1 < matSize){
            if(mat[i+1][j] > neighbor_max){
                neighbor_i = i+1;
                neighbor_j = j;
                neighbor_max = mat[i+1][j];
            }
        }

        //left
        if(j-1>= 0){
            if(mat[i][j-1] > neighbor_max ){
                neighbor_i = i;
                neighbor_j = j-1;
                neighbor_max = mat[i][j-1];
            }
        }

        //Right
        if(j+1<matColSize[i]){
            if(mat[i][j+1] > neighbor_max ){
                neighbor_i = i;
                neighbor_j = j+1;
                neighbor_max = mat[i][j+1];
            }
        }

        if(neighbor_i==-1){
            break;
        } else {
            i = neighbor_i;
            j = neighbor_j;
        }
    }
    int *ret = malloc((*returnSize)*sizeof(int));
    ret[0] = i;
    ret[1] = j;
    return ret;
}