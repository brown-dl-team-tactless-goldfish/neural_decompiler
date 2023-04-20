int minOperations(char * s){
    int len = strlen(s);
    int beginOne = 0, beginZero = 0;
    for(int i = 0; i < len; i++){
        if(i & 1){
            beginOne += (s[i]=='1')? 1 : 0;
            beginZero += (s[i]=='0')? 1 : 0;
        }
        else {
            beginOne += (s[i]=='0')? 1 : 0;
            beginZero += (s[i]=='1')? 1 : 0;
        }        
    }
    return beginOne<beginZero? beginOne :beginZero;
}