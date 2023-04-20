char * convert(char * s, int numRows){
    const int len = strlen(s);
    if(numRows == 1 || len == 1)
        return s;
    
    int sub_len;
    if(numRows == 2)
        sub_len = len/2 + len%2;
    else    
        sub_len = len/(numRows-1);
        
    int* id = calloc(numRows, sizeof(int));
    char** sub_str = malloc(numRows * sizeof(char*));
    for(int i = 0; i < numRows; i++){
        sub_str[i] = malloc((sub_len + 1) * sizeof(char));
    }
    sub_str[0][0] = s[0];
    
    id[0] = 1;
    int state = 1; 
    int pos;
    while(state < len){
        //down
        for(int i = 1; i < numRows && state < len; i++ ){
            pos = id[i];
            sub_str[i][pos] = s[state];
            state++;
            id[i]++;
        }
        //up
        for(int i = numRows-2; i >=0 && state < len ; i-- ){
            pos = id[i];
            sub_str[i][pos] = s[state];
            state++;
            id[i]++;
        }
    }
    
    pos = 0;
    for(int i = 0; i < numRows; i++){
        strncpy(&s[pos], sub_str[i], id[i]);
        pos += id[i];
    }
    for(int i = 0; i < numRows; i++){
        free(sub_str[i]);
    }
    free(sub_str);
    free(id);
    return s;
}