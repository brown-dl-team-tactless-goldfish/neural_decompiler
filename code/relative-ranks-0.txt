struct pair {
    int idx;
    int score;
};

int cmp(const void* a, const void* b) {
    struct pair pa = *(const struct pair*) a;
    struct pair pb = *(const struct pair*) b;
    return pb.score - pa.score;
}

char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    struct pair* arr = (struct pair*) calloc(scoreSize, sizeof(struct pair));  
    for (int i = 0; i < scoreSize; i++) {
        arr[i].idx = i;
        arr[i].score = score[i];
    }
    qsort(arr, scoreSize, sizeof(struct pair), cmp);
    *returnSize = scoreSize;
    char** res = (char**) malloc((*returnSize) * sizeof(char*));
    for (int i = 0; i < (*returnSize); i++) {
        res[i] = (char*) malloc(13 * sizeof(char));
    }
    for (int i = 0; i < scoreSize; i++) {
        if (i == 0) {
            res[arr[0].idx] = "Gold Medal";
        } else if (i == 1) {
            res[arr[1].idx] = "Silver Medal";
        } else if (i == 2) {
            res[arr[2].idx] = "Bronze Medal";
        } else {
            sprintf(res[arr[i].idx], "%d", i+1);
        }
    }
    free(arr);
    return res;
}