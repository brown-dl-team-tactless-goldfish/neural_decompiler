int countCharacters(char ** words, int wordsSize, char * chars){
    u_int chars_table[26] = {0};
    int i,j;
    int res = 0;
    for(i=0;chars[i];i++) chars_table[chars[i]-'a']++;
    for(i=0;i<wordsSize;i++) {
        u_int table[26] = {0};
        for(j=0;words[i][j];j++) {
            table[words[i][j]-'a']++;
        }
        for(j=0;j<26;j++) {
            if(table[j] > chars_table[j]) break;
        }
        if(j==26) res+=strlen(words[i]); 
    }
    return res;
}