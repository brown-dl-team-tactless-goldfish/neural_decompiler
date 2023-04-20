int rearrangeCharacters(char * s, char * target){
    int Table[26]={0};
    for(int i = 0; i < strlen(s); i++){
        Table[s[i]-'a']++;
    }
    
    int res = 0;
    while(1){
        int count = 0;
        for(int i = 0; i < strlen(target); i++){
            if(Table[target[i]-'a'] > 0){
                Table[target[i]-'a']--;
                count++;
            }
            else return res;
        }
        if(count == strlen(target)) res++;
    }
    return res;
}