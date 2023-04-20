int** spiralMatrixIII(int rows, int cols, int rStart, int cStart, int* returnSize, int** returnColumnSizes) {
    (*returnSize) = rows * cols;
    *returnColumnSizes = (int*) malloc((*returnSize) * sizeof(int));
    int** res = (int**) malloc((*returnSize) * sizeof(int*));
    for (int i = 0; i < (*returnSize); i++) {
        res[i] = (int*) calloc(2, sizeof(int));
        (*returnColumnSizes)[i] = 2;
    }
    res[0][0] = rStart; res[0][1] = cStart;
    int up = 1, right = 1, cntRL = 0, cntUD = 0, idx = 1;
    while (idx < (*returnSize)) {
        for (int shift = 1; shift <= right; shift++) {
            cStart = (cntRL % 2 == 0) ? cStart + 1 : cStart - 1;
            if (rStart < rows && cStart < cols && rStart > -1 && cStart > -1) {
                res[idx][0] = rStart;
                res[idx][1] = cStart;
                idx++;
            }
        }
        cntRL++;
        right++;
        for (int shift = 1; shift <= up; shift++) {
            rStart = (cntUD % 2 == 0) ? rStart + 1 : rStart - 1;
            if (rStart < rows && cStart < cols && rStart > -1 && cStart > -1) {
                res[idx][0] = rStart;
                res[idx][1] = cStart;
                idx++;
            }
        }
        cntUD++;
        up++;
    }
    return res;
}