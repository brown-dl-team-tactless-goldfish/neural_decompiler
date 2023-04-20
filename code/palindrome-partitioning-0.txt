/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void DFS(int cur, char*s, int n, char*** ans, int* a_idx, int* a_col, int** data, int d_idx, bool** dp){
    if(cur == n){
        ans[*a_idx] = malloc( d_idx * sizeof(char*) ) ;
        for(int i = 0; i < d_idx; i++){
            int l = data[i][1] - data[i][0] + 1 ;
            ans[*a_idx][i] = malloc(l + 1) ;
            ans[*a_idx][i][l] = '\0' ;
            strncpy(ans[*a_idx][i] , &s[data[i][0]] , l ) ;
        }
        a_col[*a_idx] = d_idx ;
        (*a_idx)++ ;
        return  ;
    }    
    for(int i = cur; i < n; i++){
        if(dp[cur][i] == true){
            data[d_idx][0] = cur ;
            data[d_idx][1] = i ;
            d_idx++ ;
            DFS(i+1, s, n, ans, a_idx, a_col, data, d_idx, dp) ;
            d_idx-- ;
        }
    }
}
char *** partition(char * s, int* returnSize, int** returnColumnSizes){
    int n = strlen(s) ;
    bool** dp = malloc(n * sizeof(bool*) ) ;
    for(int i = 0; i < n; i++){
        dp[i] = calloc(n, sizeof(bool)) ;
        dp[i][i] = true ;
    }
    for(int i = 0; i < n-1; i++){
        if(s[i] == s[i+1])
            dp[i][i+1] = true ;
    }
    for(int i = 3 ; i <= n; i++){
        for(int j = 0; j <= n-i; j++){
            if(s[j] == s[j+i-1] && dp[j+1][j+i-1-1])
                dp[j][j+i-1] = true ;
        }
    }
    long long N = fmin(INT_MAX, n * n* n * n) ;
    char*** ans = malloc(N *sizeof(char**) ) ;
    *returnSize =  0;
    *returnColumnSizes = malloc(N * sizeof(int) ) ;
    int** data = malloc(n * sizeof(int*) ) ;
    for(int i = 0; i < n; i++){
        data[i] = malloc(2 * sizeof(int) ) ;
    }
    DFS(0, s, n, ans, returnSize, *returnColumnSizes, data, 0, dp) ;
    ans = realloc(ans , (*returnSize) * sizeof(char**) ) ;
    for(int i = 0; i < n; i++){
        free(dp[i]) ;
        free(data[i]) ;
    }
    free(dp) ;
    free(data) ;
    *returnColumnSizes = realloc(*returnColumnSizes, (*returnSize) * sizeof(int) ) ;
    return ans ;
}