int numDistinct(char * s, char * t){
    int s_length = strlen(s), t_length = strlen(t);
    unsigned long long DP[s_length + 1][t_length + 1];

    // base case when all the chars of t were matched with those of s.
    for (int i = 0; i < s_length + 1; i++) {
        DP[i][0] = 1;
    }

    // base case when there were chars of s that did not match those of t.
    for (int j = 1; j < t_length + 1; j++) {
        DP[0][j] = 0;
    }

    for (int i = 1; i < s_length + 1; i++) {
        for (int j = 1; j < t_length + 1; j++) {
            if (s[i - 1] == t[j - 1]) {
                DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j];
            } else {
                DP[i][j] = DP[i - 1][j];
            }
        }
    }
    
    return DP[s_length][t_length];
}