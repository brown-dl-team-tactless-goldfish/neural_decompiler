char * decodeString(char * s){
    int len = strlen(s), ansIdx = 0, sIdx = -1, idx = 0;
    char* stack = (char*)calloc(10000, sizeof(char));
    while(idx < len){
        if(s[idx]!=']')
            stack[++sIdx] = s[idx];
        else{
            /* find the beginning of current string [....] 
             * copy the string into tmp 
             * find the repeat cnt than put it back to stack */
            int strEnd = sIdx;
            while(stack[sIdx]!='['){ sIdx--; }
            int strStart = sIdx + 1;
            sIdx--;
            int len = strEnd - strStart + 1;
            char* tmp = (char*)calloc(len, sizeof(char));
            memcpy(tmp, &stack[strStart], sizeof(char)*len);
            int repeatCnt = 0, multi = 1; 
            while(sIdx >= 0 && stack[sIdx]>='0' && stack[sIdx]<='9'){
                repeatCnt += ((stack[sIdx--]-'0') * multi);
                multi *= 10;
            }
            for(int i = 0; i < repeatCnt; i++)
                for(int j = 0; j < len; j++)
                    stack[++sIdx] = tmp[j];
            free(tmp);
        }
        idx++;
    }
    stack[++sIdx] = '\0';
    return stack;
}