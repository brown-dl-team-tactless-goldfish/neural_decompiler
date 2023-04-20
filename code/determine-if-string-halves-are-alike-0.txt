bool halvesAreAlike(char* s) {
    int len = strlen(s), cnt1 = 0, cnt2 = 0;
    len /= 2;
    for (int i = 0; i < len; i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' ||
            s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
            cnt1++;
        }
        if (s[i + len] == 'a' || s[i + len] == 'e' || s[i + len] == 'i' || s[i + len] == 'o' || s[i + len] == 'u' ||
            s[i + len] == 'A' || s[i + len] == 'E' || s[i + len] == 'I' || s[i + len] == 'O' || s[i + len] == 'U') {
            cnt2++;
        }
    }
    return cnt1 == cnt2;
}