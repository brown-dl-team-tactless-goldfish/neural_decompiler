int longestIdealString(char * s, int k){
    int n = strlen(s);
    int* dp = malloc(n * sizeof(int));
    int* prev = malloc( 26  * sizeof(int));
    for(int i = 0; i < n; i++){
        dp[i] = 1;
    }
    for(int i = 0; i < 26; i++){
        prev[i] = -1;
    }
    int ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = fmax(0, s[i] -'a' - k); j <= fmin(25, s[i] -'a' + k); j++ ){
            if(prev[j] != -1)
                dp[i] = fmax(dp[i] , 1 + dp[prev[j]]);
        }
        prev[s[i] - 'a'] = i;
        ans = fmax(ans, dp[i]);
    }
    
    return ans;
}