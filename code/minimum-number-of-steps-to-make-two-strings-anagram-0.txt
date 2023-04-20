int minSteps(char * s, char * t){
    int* alpha = calloc(26, sizeof(int)) ;
    for(int i = 0; i < strlen(s); i++){
        alpha[s[i] - 'a']++ ;
        alpha[t[i] - 'a']-- ;
    }
    int ret = 0 ; 
    for(int i = 0; i < 26; i++)
        if(alpha[i] > 0)
            ret += alpha[i] ;
    
    return ret ;
}