int** generate(int numRows, int* returnSize, int** returnColumnSizes) {
    *returnSize = numRows;
    int** ans = (int**) malloc(numRows * sizeof(int*));
    *returnColumnSizes = (int*) malloc(numRows * sizeof(int));
    for (int i = 0; i < numRows; i++) {
        ans[i] = (int*) malloc(numRows * sizeof(int));
        (*returnColumnSizes)[i] = i+1;
        ans[i][i] = ans[i][0] = 1;
        for (int j = 1; j < i; j++) {
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j];
        }
    }
    return ans;
}