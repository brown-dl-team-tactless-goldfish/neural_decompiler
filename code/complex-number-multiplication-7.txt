void getNum(char *a, int ab[]){
    int i;
    char buf[5];
    for(i=0;a[i]!='+';i++){
        buf[i] = a[i];
    }
    buf[i] = NULL;
    ab[0] = atoi(buf);
    int k=0;
    i++;
    while(a[i]!='i'){
        buf[k] =a[i];
        i++;
        k++;
    }
    buf[k] = NULL;
    ab[1] = atoi(buf);
    
}

void itoa(int a, char buf[]){
    if(a==0){
        buf[0] = '0';
        buf[1] = NULL;
        return;
    }
    int num = a;
    int k=0;
    num = num>=0? num:-num;
    while(num){
        buf[k++] = (num%10) + '0';
        num/=10;
    }
    if(a<0) buf[k++] = '-';
    buf[k] = NULL;
    int l=0, r = k-1;
    while(l<r){
        char temp = buf[l];
        buf[l] = buf[r];
        buf[r] = temp;
        l++;r--;
    }
}

char * complexNumberMultiply(char * a, char * b){
    int ab[2][2];
    char *ans = (char*)malloc(sizeof(char)*13);
    ans[0]=NULL;
    char buf_l[7];
    char buf_r[7];
    getNum(a, ab[0]);
    getNum(b, ab[1]);
    
    int A = (ab[0][0] * ab[1][0]) - (ab[0][1]*ab[1][1]);
    int B = (ab[0][0] * ab[1][1]) + (ab[0][1] * ab[1][0]);
    
    itoa(A, buf_l);
    itoa(B, buf_r);
    strcat(ans, buf_l);
    strcat(ans, "+");
    strcat(ans, buf_r);
    strcat(ans, "i");
    
    
    return ans;
}