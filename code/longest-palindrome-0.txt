int longestPalindrome(char * s){
    int count[58]; // ASCII A-z
    memset(count, 0x0, 58 * sizeof(int));
    int len = strlen(s);
    for (int i = 0; i < len; ++i) {
        count[s[i] - 'A']++;
    }
    int result = 0;
    for (int i = 0; i < 58; ++i) {
        result += count[i] / 2 * 2;
    }
    if (result < len) {
        result++;
    }
    
    return result;
}