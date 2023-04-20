void dfs(int** M, int MSize, int index, bool* visited) {
    visited[index] = true;
    for (int i = 0; i < MSize; ++i) {
        if (M[index][i] && !visited[i]) {
            dfs(M, MSize, i, visited);
        }
    }
}

int findCircleNum(int** M, int MSize, int* MColSize){
    int circles = 0;
    bool* visited = (bool*)calloc(MSize, sizeof(bool));
    
    for (int i = 0; i < MSize; ++i) {
        if (!visited[i]) {
            circles++;
            dfs(M, MSize, i, visited);
        }
    }
    
    
    free(visited);
    
    return circles;
}
