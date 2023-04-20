int longestCommonSubsequence(char * s, char * t){
    int dp[1005][1005],c,sl=strlen(s),tl=strlen(t),i,j,m;
    for(i=0;i<=tl;i++)dp[0][i]=0;
    for(i=0;i<=sl;i++)dp[i][0]=0;
    for(i=1;i<=sl;i++){
        for(j=1;j<=tl;j++){
            m=dp[i-1][j-1];
            if(s[i-1]==t[j-1]){
                dp[i][j]=m+1;
            }
            else dp[i][j]=fmax(fmax(m,dp[i][j-1]),dp[i-1][j]);
            c=dp[i][j];
        }
    }
    return c;
}