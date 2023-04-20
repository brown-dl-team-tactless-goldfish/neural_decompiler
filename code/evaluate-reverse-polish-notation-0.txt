int charToInt(char* s){
    int len = strlen(s);
    int ans = 0;
    bool positive = true;
    for(int i = 0; i < len; i++){
        if(s[i] == '-'){
            positive = false;  
            continue;
        }
        ans = ans*10 + s[i]-'0';
    }
    if(positive == false)
        ans = ans * -1;
    
    //printf("integer = %d  ", ans);
    return ans;
}

int evalRPN(char ** tokens, int tokensSize){
   
    long long* stack = (long long*)malloc(tokensSize * sizeof(long long));
    int index = -1;
    int i;
    long long a;
    int b;
    for(i = 0; i < tokensSize; i++){
        if(tokens[i][0] == '+'){
            a = stack[index];
            index--;
            b = stack[index];
            stack[index] = b+a;
            //printf("%d ", stack[index] );
        }
        else if(strlen(tokens[i]) == 1 && tokens[i][0] == '-'){
            a = stack[index];
            index--;
            b = stack[index];
            stack[index] = b-a;
            //printf("%d ", stack[index] );
        }
        else if(tokens[i][0] == '*'){
            a = stack[index];
            index--;
            b = stack[index];
            stack[index] = b*a;
            //printf("%d ", stack[index] );
        }
        else if(tokens[i][0] == '/'){
            a = stack[index];
            index--;
            b = stack[index];
            stack[index] = b/a;
            //printf("%d ", stack[index] );
        }
        else{
            index++;
            stack[index] = charToInt(tokens[i]);
            //printf("%d ", stack[index] );
        }            
    }
    
    int ans = stack[0];
    free(stack);
    return ans;
}