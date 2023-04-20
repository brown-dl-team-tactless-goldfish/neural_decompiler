int hash(char* s){
    int t = 0;
    for(int i = 0; i < strlen(s); i++){
        t += (s[i] -'a' + 1) * (s[i]-'a' + 1);
    }
    return t;
}
char ** removeAnagrams(char ** words, int wordsSize, int* returnSize){
    int i, j;
    
    char** ans = malloc(wordsSize * sizeof(char*));
    int idx = 0;
    
    ans[idx] = malloc((strlen(words[0]) + 1) * sizeof(char));
    strcpy(ans[idx], words[0]);
    idx++;
    
    int preHash = hash(words[0]);
    for(i = 1; i < wordsSize; i++){
        int tmepHash = hash(words[i]);
        if( tmepHash != preHash){
            preHash = tmepHash;
            ans[idx] = malloc((strlen(words[i]) + 1) * sizeof(char));
            strcpy(ans[idx], words[i]);
            idx++;                          
        }
    }
        
    * returnSize = idx;
    ans = realloc(ans, idx*sizeof(char*));
    return ans;
}