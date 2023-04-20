void check(int* edges, int* used, int start, int* count, int k, int* max){
    if (k == -1){
        return;
    }
    if (used[k] != 0){
        if (used[k] >= start){
            if (*count - used[k] > *max){
                *max = *count - used[k];
            }
        }
        return;
    }
    used[k] = *count;
    *count += 1;
    check(edges, used, start, count, edges[k], max);
}

int longestCycle(int* edges, int edgesSize){
    int* used = calloc(edgesSize,sizeof(int));
    int max = -1;
    int start = 1;
    int count = 1;
    for (int i = 0 ; i < edgesSize ; i++){
        if (used[i] == 0){
            used[i] = count;
            start = count;
            count++;
            check(edges, used, start, &count, edges[i], &max);
        }
    }
    free(used);
    return max;
}