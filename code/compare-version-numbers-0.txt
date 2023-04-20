int countDot(char* s, int n){
    int dot = 0 ;
    for(int i = 0; i < n; i++){
        if(s[i] == '.')
            dot++;
    }
    return dot ;
}

void helper(char* s, int n, int* data){
    unsigned int val = 0 ; 
    int idx = 0 ;
    for(int i = 0; i < n; i++){
        if(s[i] == '.'){
            data[idx] = val ;
            idx++;
            val = 0;
        }
        else{
            val = val*10 + s[i] - '0' ;
        }
    }
    data[idx] = val ;
}
int compareVersion(char * version1, char * version2){
    int n1 = strlen(version1) ;
    int n2 = strlen(version2) ;
    int item1 = countDot(version1, n1) + 1 ;
    int item2 = countDot(version2, n2) + 1;
    int* data1 = malloc( item1 * sizeof(int)) ;
    int* data2 = malloc( item2 * sizeof(int)) ;
    helper(version1, n1, data1) ;
    helper(version2, n2, data2) ;
    int p1 = 0, p2 = 0 ;
    int ans = 0 ;
    while(p1 < item1 || p2 < item2){
        if(p1 == item1){
            for(int i = p2; i < item2; i++){
                if(data2[i] != 0){
                    ans = -1 ;
                    goto exit ;
                }
            }
            ans = 0 ;
            goto exit ;
        }
        else if(p2 == item2){
            for(int i = p1; i < item1; i++){
                if(data1[i] != 0){
                    ans = 1 ;
                    goto exit ;
                }
            }
            ans = 0 ;
            goto exit ;
        }
        else{
            if(data1[p1] > data2[p2]){
                ans = 1 ;
                goto exit ;
            }
            if(data1[p1] < data2[p2]){
                ans = -1 ;
                goto exit ;
            }
            p1++ ;
            p2++;
        }     
    }
    exit :
    free(data1) ;
    free(data2) ;
    return ans ;
}