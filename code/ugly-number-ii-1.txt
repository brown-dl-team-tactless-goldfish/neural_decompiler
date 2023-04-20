

int nthUglyNumber(int n){
    int dp[n];
    int i = 0, j = 0, k = 0;
    int min, *m;

    dp[0] = 1;
    for (int l = 1; l < n; l++) {
        if (dp[i] * 2 < dp[j] * 3) {
            min = dp[i] * 2;
            m = &i;
        } else {
            min = dp[j] * 3;
            m = &j;
        }

        if (min > dp[k] * 5) {
            min = dp[k] * 5;
            m = &k;
        }
        
        if (dp[l - 1] != min)
            dp[l] = min;
        else
            l--;
        
        (*m)++;
    }

    return dp[n - 1];
}