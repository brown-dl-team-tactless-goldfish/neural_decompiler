long parseLong(char* n){
    long r = 0;
    for(int i = 0; n[i]; i++)
        r = r * 10 + (n[i] - '0');
    return r;
}

void minusOne(char* n) {
    while (*n == '0')
        *n-- = '9';
    (*n)--;
}

void plusOne(char* n) {
    while (*n == '9')
        *n-- = '0';
    (*n)++;
}

char* clone(char* n, int len) {
    char* t = malloc(len * sizeof(char) + 2);
    t[len + 1] = '\0';
    t[0] = '0';
    int mid = (len - 1) / 2;
    for (int i = 0; i <= mid; i++)
        t[i + 1] = n[i];
    return t;
}

char* nearestPalindromic(char* t) { // Let t = 10000
    int len = strlen(t);
    int tLen = len + 1;
    int mid = tLen / 2 ;
    
    if(len == 1) {
        --*t;
        return t;
    }
    
    char* t1 = clone(t, len);       // t1 = 0100??
    char* t2 = clone(t, len);       // t2 = 0100??
    char* t3 = clone(t, len);       // t3 = 0100??
    
    //Mid
    int left = 1, right = tLen - 1;
    for (int i = 0; i <= mid; i++)  
        t1[right - i] = t1[left + i];//t1 = 010001

    //Less
    minusOne(t2 + mid);              //t2 = 0099??
    for (int i = 0; i <= mid; i++) 
        t2[right - i] = t2[left + i];//t2 = 009990

    if (t2[left] == '0')
        t2[right] = '9';             //t2 = 009999

    //Greater
    plusOne(t3 + mid);               //t3 = 0101??
    if(*t3 != '0') left = 0;         //This part is for the cases: 09 + 1 = 10, 099 + 1 = 100, and so on.
    for (int i = 0; i <= mid; i++)
        t3[right - i] = t3[left + i];//t3 = 010101
    
    long ln  = parseLong(t); 
    long ln1 = parseLong(t1) /*mid*/    , diff1 = abs(ln1 - ln); 
    long ln2 = parseLong(t2) /*less*/   , diff2 = abs(ln2 - ln); 
    long ln3 = parseLong(t3) /*greater*/, diff3 = abs(ln3 - ln); 
    
    char* res;
    if (ln > ln1)
        res = diff1 > diff3 ? t3 : t1;
    else if (ln < ln1)
        res = diff2 > diff1 ? t1 : t2;
    else
        res = diff2 > diff3 ? t3 : t2;
    
    while (*res == '0') res++;

    return res;
}