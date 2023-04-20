int maxVal(int a, int b) {
    return a > b ? a : b;
}

int extend(char *s, int start, int end) {
    int len = strlen(s);
    for(; start >= 0 && end < len; start--, end++) {
        if(*(s + start) != *(s + end))
            break;
    }
    return end - start - 1;
}

char * longestPalindrome(char * s){
    int max = 0, idx = 0, len = strlen(s);
    for(int i = 0; i < len; i++) {
        int len1 = extend(s, i, i);       /* For even string */
        int len2 = extend(s, i, i + 1);   /* For odd string  */
        if (max < maxVal(len1, len2)) {
            idx = (len1 > len2) ? (i - len1 / 2) : (i - len2 / 2 + 1);
            max = maxVal(len1, len2);
        }
    }
    char *res = malloc((max+1) *sizeof(char));
    memcpy(res, &s[idx], max);
    res[max] = '\0';
    return res;
}