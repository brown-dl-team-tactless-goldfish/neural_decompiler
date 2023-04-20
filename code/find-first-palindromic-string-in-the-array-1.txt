bool checkPal(char *s){
    int i = 0, j = strlen(s) - 1;
    
    while(i < j){
        if(s[i] != s[j])
            return 0;
        
        i++;
        j--;
    }
    return 1;
}

char * firstPalindrome(char ** words, int wordsSize){
    int i;
    
    for(i = 0; i < wordsSize; i++){
        if(checkPal(words[i]))
            return words[i];
    }
    
    return "";
}