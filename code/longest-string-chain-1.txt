int cmp(const void *a, const void *b)
{
    return strlen(*(char **)a) - strlen(*(char **)b);
}

bool canConn(char * from, char * to) 
{
    if(strlen(to) - strlen(from) != 1) return false;
    int ti = 0, fi = 0;
    while(ti < strlen(to) && fi < strlen(from))
    {
        if(from[fi] == to[ti])
        {
            ti++;
            fi++;
        }
        else ti++;
    }
    return fi == strlen(from);
}

int longestStrChain(char ** words, int wordsSize){
    qsort(words, wordsSize, sizeof(char *), cmp);
    int dp[wordsSize], result = 1;
    for(int i = 0; i < wordsSize; i++)
        dp[i] = 1;
    for(int i = 1; i < wordsSize; i++)
    {
        for(int j = 0; j < i; j++) 
        {
            if(canConn(words[j], words[i]))
                dp[i] = dp[i] > dp[j] + 1 ? dp[i] : dp[j] + 1;    
        }
        result = result > dp[i] ? result : dp[i];
    }
    return result;
}