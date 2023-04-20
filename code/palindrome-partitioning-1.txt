bool palindrome (char* s, int head, int end){
    for (int i = head ; head < end ; head++,end--){
        if (s[head] != s[end]){
            return false;
        }
    }
    return true;
}

void inputlist (char* s, int head, int end, char** list,int count, int* LONG){
    LONG[count] = end-head+1;
    strncpy(list[count], s+head, LONG[count]);
}

void inputans (char* s, char** list,int count, int* LONG, char*** ans, int* returnSize, int** returnColumnSizes, int now, int len, int** canpalindrome, int* eachcount) {
    if (now == len){
        ans[*returnSize] = malloc(sizeof(char*)*count);
        for (int k = 0 ; k < count ; k++){
            ans[*returnSize][k] = malloc(sizeof(char)*(LONG[k]+1));
            strncpy(ans[*returnSize][k], list[k], LONG[k]);
            ans[*returnSize][k][LONG[k]] = '\0';
        }
        (*returnColumnSizes)[*returnSize] = count;
        *returnSize += 1;
        return;
    }
    for (int i = 0 ; i < eachcount[now] ; i++){
        inputlist ( s, now, canpalindrome[now][i], list, count, LONG);
        inputans ( s, list, count+1, LONG, ans, returnSize, returnColumnSizes,
                  canpalindrome[now][i]+1, len, canpalindrome, eachcount);
    }
}

char *** partition(char * s, int* returnSize, int** returnColumnSizes){
    int len = strlen(s);
    int** canpalindrome = malloc(sizeof(int*)*16);
    for (int i = 0 ; i < 16 ; i++){
        canpalindrome[i] = malloc(sizeof(int)*16);
    }
    int eachcount[16] = {0};
    for (int i = 0 ; i < len ; i++){
        for (int j = i ; j < len ; j++){
            if (s[i] == s[j] && palindrome(s,i+1,j-1)){
                canpalindrome[i][eachcount[i]] = j;
                eachcount[i]++;
            }
        }
    }
    
    char*** ans = malloc(sizeof(char**)*40000);
    *returnSize = 0;
    (*returnColumnSizes) = malloc(sizeof(int)*40000);
    
    char** list = malloc(sizeof(char*)*16);
    for(int i = 0 ; i < 16 ; i++){
        list[i] = malloc(sizeof(char)*16);
    }
    
    int LONG[16] = {0};
    
    for (int i = 0 ; i < eachcount[0] ; i++){
        inputlist (s, 0, canpalindrome[0][i], list, 0, LONG);
        inputans ( s, list, 1, LONG, ans, returnSize, returnColumnSizes, 
                  canpalindrome[0][i]+1, len, canpalindrome, eachcount);
    }
    
    for (int i = 0 ; i < 16 ; i++){
        free(canpalindrome[i]);
    }
     free(canpalindrome);
    return ans;
}