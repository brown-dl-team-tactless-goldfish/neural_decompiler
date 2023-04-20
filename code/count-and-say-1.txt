char* countAndSay(int n)
{
    if(n == 1)
    {
        return "1";
    }
    // get s
    char* s = countAndSay(n - 1);  // answer from previous call
    int size = strlen(s);  // size of s
    // get ans
    char* ans = (char*) malloc(4463 * sizeof(char));
    // iterate through s and add to ans
    int idx = 0;  // idx in ans
    char curr = *s;  // first char of s
    int cnt = 1;  // count of curr
    for(int i = 1; i < size; i++)
    {
        char c = *(s + i);
        if(c == curr)
        {
            cnt++;
        }
        else
        {
            *(ans + idx++) = ('0' + cnt);
            *(ans + idx++) = curr;
            curr = c;
            cnt = 1;
        }
        // printf("%s\n", ans);
    }
    *(ans + idx++) = ('0' + cnt);
    *(ans + idx++) = curr;
    *(ans + idx) = '\0';
    // ans = (char*) realloc(ans, (idx + 1) * sizeof(char));
    return ans;
}