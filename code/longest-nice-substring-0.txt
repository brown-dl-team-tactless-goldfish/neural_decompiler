void helper(char* s, int n, int* max, char* ans){
    if(n <= (*max) || n < 2)
        return;
    int* cn = calloc(52, sizeof(int));
    for(int i = 0; i < n; i++){
        if(s[i] >= 'a')
            cn[s[i] - 'a']++;
        else
            cn[s[i] - 'A' + 26]++;
    } 
    int start  = 0;
    int i;
    for(i = 0; i < n; i++){
        if(s[i] >= 'a' ){
            if(cn[s[i] - 'a' + 26] == 0){
                helper(s, i, max, ans);
                helper(&s[i+1], n-1-i, max, ans);
                break;
            }
        }
        else{
            if(cn[s[i] - 'A'] == 0){
                helper(&s[0], i, max, ans);
                helper(&s[i+1], n-1-i, max, ans);
                break;
            }
        }
    }
    if(i == n){
        if(n > (*max)){
            *max = n;            
            strncpy(ans, s, n);
            ans[n] = '\0';
        }
    }
}

char * longestNiceSubstring(char * s){
    int n = strlen(s);
    int max = 0;
    char* ans = malloc( (n+1) * sizeof(char));
    ans[0] = '\0';
    helper(s, n, &max, ans);
    return ans;
}