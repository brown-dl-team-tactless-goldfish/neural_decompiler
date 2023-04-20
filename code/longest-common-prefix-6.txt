char * longestCommonPrefix(char ** strs, int strsSize)
{
    int count = 0;
    char buf[255];

    if (strsSize == 0)
        goto END;

    for (int i = 0; i < 255; i++)
    {
        for (int j = 0; j < strsSize; j++)
            if (strs[j][i] == NULL || (j > 0 && strs[j-1][i] != strs[j][i]))
                goto END;

        buf[count++] = strs[0][i];
    }
    END: buf[count] = '\0';

    char *result = (char *) malloc(sizeof(char) * (count + 1));
    strcpy(result, buf);
    return result;
}