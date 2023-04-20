int cmp(const void* a, const void* b) {
    return *(const int*) a - *(const int*) b;
}

int** findWinners(int** matches, int matchesSize, int* matchesColSize, int* returnSize, int** returnColumnSizes) {
    int loserARR[100001] = {0};
    *returnSize = 2;
    int** res = (int**) malloc((*returnSize) * sizeof(int*));
    *returnColumnSizes = (int*) calloc((*returnSize), sizeof(int));
    for (int i = 0; i < (*returnSize); i++) {
        res[i] = (int*) malloc(matchesSize * sizeof(int));
    }
    for (int i = 0; i < matchesSize; i++) {
        loserARR[matches[i][1]]++;
    }
    for (int i = 0; i < matchesSize; i++) {
        if (loserARR[matches[i][1]] == 1) res[1][(*returnColumnSizes)[1]++] = matches[i][1];
        if (loserARR[matches[i][0]] == 0) {
            res[0][(*returnColumnSizes)[0]++] = matches[i][0];
            loserARR[matches[i][0]] = -1;
        }
    }
    qsort(res[0], (*returnColumnSizes)[0], sizeof(int), cmp);
    qsort(res[1], (*returnColumnSizes)[1], sizeof(int), cmp);
    return res;
}